---
title: "3.2 Tạo SonarQube server (EC2)"
date: 2025-01-01
weight: 2
---

## Tạo SonarQube server trên EC2

Vào **AWS Console -> EC2 -> Launch Instance**:

| Mục | Giá trị |
|-----|---------|
| Name | `SonarServer` |
| AMI / OS | Ubuntu Server (LTS mới nhất) |
| Instance type | **t2.medium** (tối thiểu 4 GB RAM) |
| Key pair | Tạo mới `SonarKey` |
| Security group | Tạo mới `sonar-sg` |

Security group `sonar-sg`: mở **port 22** (My IP) và **port 80** (Anywhere).

{{% notice info %}}
Truy cập SonarQube qua **port 80** (Nginx proxy về `127.0.0.1:9000`). Bảo mật bằng token nên mở
port 80 ra internet là chấp nhận được cho workshop.
{{% /notice %}}

Dán script sau vào **Advanced details -> User data** (tự cài Java 21, PostgreSQL, SonarQube 26.4,
Nginx rồi reboot):

```bash
#!/bin/bash
cp /etc/sysctl.conf /root/sysctl.conf_backup
cat <<EOT> /etc/sysctl.conf
vm.max_map_count=262144
fs.file-max=65536
EOT
sysctl -p
cp /etc/security/limits.conf /root/sec_limit.conf_backup
cat <<EOT> /etc/security/limits.conf
sonarqube - nofile 65536
sonarqube - nproc 4096
EOT
sudo apt-get update -y
sudo apt-get install openjdk-21-jdk -y
sudo update-alternatives --config java
sudo apt update
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt install postgresql postgresql-contrib -y
sudo systemctl enable --now postgresql.service
sudo echo "postgres:admin123" | chpasswd
runuser -l postgres -c "createuser sonar"
sudo -i -u postgres psql -c "ALTER USER sonar WITH ENCRYPTED PASSWORD 'admin123';"
sudo -i -u postgres psql -c "CREATE DATABASE sonarqube OWNER sonar;"
sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sonarqube to sonar;"
systemctl restart postgresql
sudo mkdir -p /sonarqube/
cd /sonarqube/
sudo curl -O https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-26.4.0.121862.zip
sudo apt-get install zip -y
sudo unzip -o sonarqube-26.4.0.121862.zip -d /opt/
sudo mv /opt/sonarqube-26.4.0.121862 /opt/sonarqube
sudo groupadd sonar
sudo useradd -c "SonarQube - User" -d /opt/sonarqube/ -g sonar sonar
sudo chown sonar:sonar /opt/sonarqube/ -R
sudo chmod 1777 /tmp
cat <<EOT> /opt/sonarqube/conf/sonar.properties
sonar.jdbc.username=sonar
sonar.jdbc.password=admin123
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
sonar.web.host=0.0.0.0
sonar.web.port=9000
sonar.web.javaAdditionalOpts=-server -Xmx1024m
sonar.search.javaOpts=-Xmx512m -Xms512m
sonar.log.level=INFO
sonar.path.logs=logs
EOT
cat <<EOT> /etc/systemd/system/sonarqube.service
[Unit]
Description=SonarQube service
After=syslog.target network.target
[Service]
Type=forking
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
User=sonar
Group=sonar
Restart=always
LimitNOFILE=65536
LimitNPROC=4096
[Install]
WantedBy=multi-user.target
EOT
systemctl daemon-reload
systemctl enable sonarqube.service
apt-get install nginx -y
rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default
cat <<EOT> /etc/nginx/sites-available/sonarqube
server{
    listen 80;
    server_name sonarqube.groophy.in;
    location / {
        proxy_pass http://127.0.0.1:9000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto http;
    }
}
EOT
ln -s /etc/nginx/sites-available/sonarqube /etc/nginx/sites-enabled/sonarqube
systemctl enable nginx.service
sudo ufw allow 80,9000/tcp
echo "SonarQube installation completed. Rebooting in 15 seconds..."
sleep 15
reboot
```

Bấm **Launch Instance** và chờ **5-10 phút** để script chạy xong và reboot.
