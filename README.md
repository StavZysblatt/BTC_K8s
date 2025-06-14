# BTC Kubernetes Project 🪙☁️

This project demonstrates deploying a Bitcoin price tracking web service and a health-check API to a local Kubernetes cluster using Minikube. It includes:

- FastAPI-based services
- Dockerized deployments
- Ingress routing
- Namespace isolation
- Network policies
- Highly available, scalable architecture

---

## 📦 Services

### Service A – Bitcoin Price API
- Exposes `/price`
- Returns:
  - `current_price`: latest Bitcoin price (updated every 60 seconds)
  - `average`: average over the last 10 minutes

### Service B – Health Check API
- Exposes `/health`
- Always returns: `{ "status": "ok" }`

---

## ⚙️ Kubernetes Features

- **4 Namespaces**: dev/prod for both services
- **Ingress (nginx)**: Routes to both services via `localhost`
- **Network Policies**: Service A cannot access Service B
- **Secrets**: External API key is injected via Kubernetes Secret
- **Highly Available**: 2 replicas per deployment
- **Minikube Tunnel**: Used to expose services via Ingress

---

## 🚀 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

##🐳 Build Docker Images Inside Minikube

eval $(minikube docker-env)

docker build -t service-a:latest ./service-a
docker build -t service-b:latest ./service-b

## Testing 
curl http://localhost/service-a/price
curl http://localhost/service-b/health


### Clone and Run

```bash
git clone https://github.com/<your-username>/BTC_K8s.git
cd BTC_K8s
minikube start
minikube tunnel
kubectl apply -f k8s/


