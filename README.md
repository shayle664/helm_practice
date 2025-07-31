# Flask App - Helm Chart

This chart deploys a Flask application on K3s using Helm.

## Prerequisites

- K3s cluster with containerd
- Flask image imported into containerd

## Build & Import Docker Image (on K3s node)

```bash
docker build -t flask-app .
docker save flask-app > /tmp/flask-app.tar
ctr images import /tmp/flask-app.tar
```

## Install with Helm

```bash
helm install flask-app ./flask-chart
```

## Access the App

```bash
NODE_PORT=$(kubectl get svc flask-app-flask-chart -o jsonpath="{.spec.ports[0].nodePort}")
NODE_IP=$(kubectl get nodes -o jsonpath="{.items[0].status.addresses[0].address}")
echo "http://$NODE_IP:$NODE_PORT"
```
