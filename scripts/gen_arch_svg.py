#!/usr/bin/env python3
"""Build a clean standalone SVG architecture diagram with original service logos."""
import base64, html, pathlib

LOGOS = pathlib.Path("docs/images/logos")
OUT = pathlib.Path("docs/images/architecture.svg")

def uri(name):
    b = base64.b64encode((LOGOS / f"{name}.svg").read_bytes()).decode()
    return f"data:image/svg+xml;base64,{b}"

W, H = 1600, 820
s = []
def add(x): s.append(x)

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">')
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
add('<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">'
    '<path d="M0,0 L7,3 L0,6 Z" fill="#5A6B7B"/></marker>'
    '<marker id="arrg" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">'
    '<path d="M0,0 L7,3 L0,6 Z" fill="#1A9C37"/></marker>'
    '<marker id="arrb" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">'
    '<path d="M0,0 L7,3 L0,6 Z" fill="#2D72D9"/></marker></defs>')

# Title
add(f'<text x="40" y="46" font-size="28" font-weight="bold" fill="#1A2330">vProfile GitOps CI/CD on AWS EKS</text>')
add(f'<text x="42" y="72" font-size="15" fill="#5A6B7B">Two GitHub Actions flows: scan on pull request, build and ship on merge - then ArgoCD syncs the Helm chart to EKS</text>')
add(f'<line x1="42" y1="88" x2="{W-40}" y2="88" stroke="#FF9900" stroke-width="2"/>')

def zone(x, y, w, h, label, color, dash=False, fill="#ffffff"):
    d = 'stroke-dasharray="6 5" ' if dash else ''
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" fill-opacity="0.5" '
        f'stroke="{color}" stroke-width="1.6" {d}/>')
    add(f'<text x="{x+16}" y="{y+24}" font-size="14" font-weight="bold" fill="{color}">{html.escape(label)}</text>')

def tile(cx, y, name, label, sub="", sz=48):
    add(f'<image x="{cx-sz//2}" y="{y}" width="{sz}" height="{sz}" href="{uri(name)}"/>')
    add(f'<text x="{cx}" y="{y+sz+15}" font-size="12" font-weight="bold" fill="#1A2330" '
        f'text-anchor="middle">{html.escape(label)}</text>')
    if sub:
        add(f'<text x="{cx}" y="{y+sz+30}" font-size="11" font-style="italic" fill="#6B7886" '
            f'text-anchor="middle">{html.escape(sub)}</text>')

def actor(cx, y, label1, label2):
    # simple laptop glyph + label
    add(f'<rect x="{cx-34}" y="{y}" width="68" height="58" rx="8" fill="#F5F6F8" stroke="#8A98A6"/>')
    add(f'<rect x="{cx-20}" y="{y+12}" width="40" height="26" rx="2" fill="#37475A"/>')
    add(f'<rect x="{cx-26}" y="{y+40}" width="52" height="5" rx="2" fill="#37475A"/>')
    add(f'<text x="{cx}" y="{y+74}" font-size="12" font-weight="bold" fill="#1A2330" text-anchor="middle">{html.escape(label1)}</text>')
    if label2:
        add(f'<text x="{cx}" y="{y+89}" font-size="12" font-weight="bold" fill="#1A2330" text-anchor="middle">{html.escape(label2)}</text>')

def arrow(pts, label="", color="#5A6B7B", dash=False, mk="arr", lx=None, ly=None):
    d = "M " + " L ".join(f"{x},{y}" for x, y in pts)
    da = 'stroke-dasharray="6 4" ' if dash else ''
    add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.8" {da}marker-end="url(#{mk})"/>')
    if label:
        if lx is None:
            lx = sum(p[0] for p in pts)/len(pts); ly = sum(p[1] for p in pts)/len(pts)
        w = 7*len(label)+10
        add(f'<rect x="{lx-w/2:.0f}" y="{ly-11}" width="{w}" height="16" rx="3" fill="#ffffff" fill-opacity="0.92"/>')
        add(f'<text x="{lx}" y="{ly+1}" font-size="11" fill="#33414F" text-anchor="middle">{html.escape(label)}</text>')

# ---- Zones ----
zone(250, 150, 380, 470, "CI / CD  -  GitHub Actions", "#5B6770", fill="#F7F9FB")
zone(900, 122, 660, 600, "AWS Cloud   |   us-east-1", "#232F3E", fill="#F6F8FB")
zone(1070, 188, 470, 500, "Amazon EKS Cluster", "#1F9CA0", dash=True, fill="#F1FAFA")

# ---- Actors ----
actor(95, 300, "Admin /", "Developer")
actor(95, 560, "End User", "")

# ---- CI tiles (2 cols x 3 rows) ----
ciL, ciR = 345, 515
tile(ciL, 210, "github", "GitHub", "app/helm/infra")
tile(ciR, 210, "githubactions", "GitHub Actions", "pipeline")
tile(ciL, 360, "docker", "Docker", "build image")
tile(ciR, 360, "sonarqube", "SonarQube", "scan (EC2)")
tile(ciL, 500, "helm", "Helm", "chart")
tile(ciR, 500, "slack", "Slack", "notify")

# ---- Terraform (provisioner) ----
tile(760, 320, "terraform", "Terraform", "provisions EKS")

# ---- AWS left column ----
awsx = 950
tile(awsx, 200, "aws_ecr", "Amazon ECR", "image")
tile(awsx, 360, "aws_acm", "ACM", "HTTPS cert")
tile(awsx, 520, "aws_elb", "ALB", "Ingress")

# ---- EKS workloads ----
c1, c2, c3 = 1140, 1300, 1460
tile(c1, 250, "kubernetes", "Kubernetes")
tile(c2, 250, "argo", "ArgoCD", "sync")
tile(c3, 250, "aws_eks", "EKS", "cluster")
tile(c1, 410, "tomcat", "vproapp", "Tomcat")
tile(c2, 410, "mysql", "vprodb", "MySQL")
tile(c3, 410, "aws_ebs", "EBS", "gp2 PVC")
tile(c1, 560, "memcached", "vprocache01", "Memcached")
tile(c2, 560, "rabbitmq", "vpromq01", "RabbitMQ")

# ---- Arrows (clean lanes) ----
arrow([(132, 300), (200, 300), (200, 234), (321, 234)], "git push / open PR", lx=222, ly=292)
# Flow 1 (blue) - on pull request: GitHub Actions -> SonarQube scan + quality gate
arrow([(539, 250), (562, 250), (562, 384), (539, 384)], "scan + quality gate",
      color="#2D72D9", mk="arrb", lx=515, ly=318)
# Flow 2 (gray) - on merge to main: build image -> ECR, then bump Helm values.yaml
arrow([(540, 222), (940, 222)], "build & push image", lx=735, ly=214)             # gha -> ecr
arrow([(489, 234), (373, 234)], "update values.yaml", lx=431, ly=222)             # gha -> github
arrow([(974, 224), (1040, 224), (1040, 250), (1116, 250)], "pull image", lx=1040, ly=212) # ecr -> k8s
arrow([(800, 332), (1035, 332), (1035, 410), (1072, 410)], "provision", color="#7B42BC", dash=True, lx=1035, ly=372) # terraform -> eks
arrow([(1300, 226), (1300, 110), (345, 110), (345, 186)], "ArgoCD sync (GitOps)", color="#1A9C37", mk="arrg", lx=820, ly=102) # argo -> github
arrow([(963, 410), (963, 520)], "TLS", color="#DD344C", dash=True, lx=980, ly=468) # acm -> alb
arrow([(974, 544), (1045, 544), (1045, 434), (1116, 434)], "route", lx=1045, ly=500) # alb -> vproapp
arrow([(95, 620), (95, 700), (905, 700), (905, 545), (944, 545)], "HTTPS", lx=480, ly=692) # user -> alb

# ---- Legend: the two GitHub Actions flows ----
def legend(y, color, text):
    add(f'<rect x="266" y="{y}" width="13" height="13" rx="2" fill="{color}"/>')
    add(f'<text x="288" y="{y+11}" font-size="11.5" fill="#33414F">{html.escape(text)}</text>')

legend(632, "#2D72D9", "On pull request: build, test, SonarQube scan + quality gate (fail blocks merge)")
legend(654, "#5A6B7B", "On merge to main: Docker build, push to ECR, then update Helm values.yaml")

add('</svg>')
OUT.write_text("\n".join(s), encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
