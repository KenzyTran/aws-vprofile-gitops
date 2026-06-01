#!/usr/bin/env python3
"""Generate a clean vProfile GitOps draw.io diagram with original service logos."""
import base64, html, pathlib

LOGO_DIR = pathlib.Path("docs/images/logos")
OUT = pathlib.Path("docs/images/architecture.drawio")

def b64(name):
    data = (LOGO_DIR / f"{name}.svg").read_bytes()
    return base64.b64encode(data).decode()

PTS = ("points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],"
       "[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],"
       "[1,0.5,0],[1,0.75,0]]")

cells = []

def esc(label, sub):
    v = html.escape(label)
    if sub:
        v += "&lt;div&gt;&lt;i&gt;" + html.escape(sub) + "&lt;/i&gt;&lt;/div&gt;"
    return v

def logo(cid, x, y, label, sub="", name=None, size=54):
    img = f"data:image/svg+xml;base64,{b64(name or cid)}"
    style = (f"shape=image;html=1;imageAspect=0;aspect=fixed;verticalLabelPosition=bottom;"
             f"verticalAlign=top;labelPosition=center;align=center;fontSize=12;fontStyle=1;"
             f"fontFamily=Helvetica;spacingTop=2;image={img};")
    cells.append(
        f'<mxCell id="{cid}" style="{style}" value="{esc(label, sub)}" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="{size}" height="{size}" as="geometry"/></mxCell>')

def aws(cid, shape, x, y, label, sub="", color="#ED7100"):
    style = (f"sketch=0;{PTS};outlineConnect=0;fontColor=#232F3E;fillColor={color};"
             f"strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;"
             f"align=center;html=1;fontSize=12;fontStyle=1;aspect=fixed;"
             f"shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{shape};fontFamily=Helvetica;")
    cells.append(
        f'<mxCell id="{cid}" style="{style}" value="{esc(label, sub)}" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="48" height="48" as="geometry"/></mxCell>')

def actor(cid, x, y, label):
    cells.append(
        f'<mxCell id="{cid}-box" style="fillColor=#f5f5f5;strokeColor=#666666;rounded=1;'
        f'whiteSpace=wrap;html=1;verticalAlign=top;fontStyle=1;fontSize=12;fontColor=#333333;'
        f'fontFamily=Helvetica;shadow=1;" value="{html.escape(label)}" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="110" height="96" as="geometry"/></mxCell>')
    style = (f"sketch=0;{PTS};outlineConnect=0;fontColor=#232F3E;fillColor=#232F3D;"
             f"strokeColor=#ffffff;dashed=0;html=1;aspect=fixed;shape=mxgraph.aws4.resourceIcon;"
             f"resIcon=mxgraph.aws4.users;fontFamily=Helvetica;")
    cells.append(
        f'<mxCell id="{cid}" style="{style}" value="" vertex="1" parent="{cid}-box">'
        f'<mxGeometry x="31" y="34" width="48" height="48" as="geometry"/></mxCell>')

def zone(cid, x, y, w, h, label, stroke, fill, grIcon=None, dashed=0):
    if grIcon:
        style = (f"points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],"
                 f"[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];"
                 f"outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=14;"
                 f"fontStyle=1;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.{grIcon};"
                 f"strokeColor={stroke};fillColor={fill};verticalAlign=top;align=left;"
                 f"spacingLeft=30;fontColor={stroke};dashed={dashed};container=0;pointerEvents=0;")
    else:
        style = (f"rounded=1;arcSize=4;html=1;whiteSpace=wrap;fontSize=14;fontStyle=1;"
                 f"verticalAlign=top;align=left;spacingLeft=14;spacingTop=8;strokeColor={stroke};"
                 f"fillColor={fill};fontColor={stroke};dashed={dashed};container=0;pointerEvents=0;"
                 f"fontFamily=Helvetica;")
    cells.append(
        f'<mxCell id="{cid}" style="{style}" value="{html.escape(label)}" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

def edge(cid, s, t, label="", pts=None, dashed=0, color="#545B64",
         exit=None, entry=None):
    g = "exitX={};exitY={};exitDx=0;exitDy=0;".format(*exit) if exit else ""
    g += "entryX={};entryY={};entryDx=0;entryDy=0;".format(*entry) if entry else ""
    style = (f"edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;"
             f"strokeColor={color};strokeWidth=1.6;dashed={dashed};{g}")
    pt = ""
    if pts:
        pt = "<Array as=\"points\">" + "".join(
            f'<mxPoint x="{px}" y="{py}"/>' for px, py in pts) + "</Array>"
    cells.append(
        f'<mxCell id="{cid}" style="{style}" edge="1" parent="1" source="{s}" target="{t}">'
        f'<mxGeometry relative="1" as="geometry">{pt}</mxGeometry></mxCell>')
    if label:
        cells.append(
            f'<mxCell id="{cid}-l" value="{html.escape(label)}" style="edgeLabel;html=1;'
            f'align=center;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=#ffffff;'
            f'fontFamily=Helvetica;fontSize=11;" connectable="0" vertex="1" parent="{cid}">'
            f'<mxGeometry relative="1" x="0" y="0" as="geometry"><mxPoint as="offset"/></mxGeometry></mxCell>')

# ---- Title ----
cells.append('<mxCell id="t1" value="vProfile GitOps CI/CD on AWS EKS" style="text;html=1;'
             'align=left;verticalAlign=top;fontSize=28;fontStyle=1;fontFamily=Helvetica;" '
             'vertex="1" parent="1"><mxGeometry x="40" y="30" width="900" height="40" as="geometry"/></mxCell>')
cells.append('<mxCell id="t2" value="Two GitHub Actions flows: scan on pull request, build and ship '
             'on merge - then ArgoCD syncs the Helm chart to EKS" style="text;html=1;align=left;verticalAlign=top;fontSize=15;'
             'fontColor=#5A6B7B;fontFamily=Helvetica;" vertex="1" parent="1">'
             '<mxGeometry x="40" y="72" width="900" height="24" as="geometry"/></mxCell>')
cells.append('<mxCell id="t3" style="line;strokeWidth=2;html=1;strokeColor=#FF9900;" vertex="1" '
             'parent="1"><mxGeometry x="42" y="100" width="1620" height="8" as="geometry"/></mxCell>')

# ---- Zones (decoration, drawn first so they sit behind) ----
zone("aws-cloud", 900, 150, 770, 640, "AWS Cloud  -  us-east-1", "#232F3E",
     "none", grIcon="group_aws_cloud")
zone("eks-box", 1130, 205, 510, 560, "Amazon EKS Cluster  (VPC, public subnets)", "#00A4A6",
     "none", grIcon="group_region", dashed=1)
zone("ci-box", 270, 188, 420, 470, "CI / CD  -  GitHub Actions", "#6C7A89",
     "none")

# ---- Actors ----
actor("admin", 60, 300, "Admin / Developer")
actor("enduser", 60, 648, "End User")

# ---- CI/CD logos ----
logo("github", 320, 232, "GitHub", "app / helm / infra")
logo("gha", 520, 232, "GitHub Actions", "pipeline", name="githubactions")
logo("docker", 320, 408, "Docker", "build image")
logo("helm", 520, 408, "Helm", "chart")
logo("slack", 420, 560, "Slack", "notify")

# ---- Middle standalone ----
aws("ec2sonar", "ec2", 786, 244, "SonarQube", "on EC2")
logo("terraform", 778, 612, "Terraform", "provisions EKS")

# ---- AWS left column ----
aws("ecr", "ecr", 952, 232, "Amazon ECR", "vprofileappimg")
aws("acm", "certificate_manager_3", 952, 410, "ACM", "HTTPS cert", color="#DD344C")
aws("alb", "elastic_load_balancing", 952, 580, "ALB", "Ingress", color="#8C4FFF")

# ---- EKS workloads ----
logo("k8s", 1168, 252, "Kubernetes", name="kubernetes")
logo("argo", 1338, 252, "ArgoCD", "GitOps CD")
logo("tomcat", 1168, 424, "vproapp", "Tomcat")
logo("mysql", 1338, 424, "vprodb", "MySQL")
aws("ebs", "elastic_block_store", 1510, 430, "EBS", "gp2", color="#3F8624")
logo("memcached", 1168, 596, "vprocache01", "Memcached")
logo("rabbitmq", 1338, 596, "vpromq01", "RabbitMQ")

# ---- Edges (dedicated lanes, no overlap) ----
edge("e1", "admin", "github", "git push", entry=(0, 0.5))
edge("e3", "gha", "ecr", "build & push image (on merge)", pts=[(740, 212), (976, 212)],
     exit=(0.5, 0), entry=(0.5, 0))
edge("e2", "gha", "ec2sonar", "scan + quality gate (on PR)", color="#2D72D9", exit=(1, 0.5), entry=(0, 0.5))
edge("e4", "gha", "github", "update values.yaml (on merge)", exit=(0, 0.8), entry=(1, 0.8))
edge("e10", "argo", "github", "ArgoCD sync (GitOps)", pts=[(1365, 112), (347, 112)],
     exit=(0.5, 0), entry=(0.5, 0), color="#1A9C37")
edge("e6", "ecr", "k8s", "pull image", pts=[(1105, 256)], exit=(1, 0.5), entry=(0, 0.5))
edge("e5", "terraform", "k8s", "provision", pts=[(1085, 639), (1085, 300)],
     exit=(1, 0.5), entry=(0, 1), color="#7B42BC", dashed=1)
edge("e9", "acm", "alb", "TLS cert", color="#DD344C", dashed=1, exit=(0.5, 1), entry=(0.5, 0))
edge("e8", "alb", "tomcat", "route", pts=[(1092, 604), (1092, 448)], exit=(1, 0.5), entry=(0, 0.5))
edge("e7", "enduser", "alb", "HTTPS", pts=[(115, 732), (905, 732), (905, 604)],
     exit=(0.5, 1), entry=(0, 0.5))

XML = ('<mxfile host="Electron" version="29.6.1"><diagram name="vProfile-GitOps" id="vp-gitops">'
       '<mxGraphModel dx="1400" dy="900" grid="0" gridSize="10" guides="1" tooltips="1" '
       'connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="1720" pageHeight="840" '
       'math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
       + "".join(cells) + '</root></mxGraphModel></diagram></mxfile>')

OUT.write_text(XML, encoding="utf-8")
print(f"wrote {OUT} ({len(XML)} bytes, {len(cells)} cells)")
