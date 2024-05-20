## Install Helm chart

Create cluster
```sh
kind create cluster
```

Install a helm chart
```sh
gtpscript helm.gpt
```

## Fix cluster

Create cluster
```sh
kind create cluster
```
Brake cluster
```sh
kubectl apply -f https://gist.githubusercontent.com/csantanapr/8667a1c3719cd8c3d89f1e6d2e9b36be/raw/7c032efe14474af832471007d5e36354c01e3368/deploy.yaml
```
Fix cluster
```sh
gptscript fix-cluster.gpt
```

