## Fix a kind cluster

Create cluster
```shell
kind create cluster
```

Brake cluster
```shell
kubectl apply -f https://gist.githubusercontent.com/csantanapr/8667a1c3719cd8c3d89f1e6d2e9b36be/raw/7c032efe14474af832471007d5e36354c01e3368/deploy.yaml
```

Fix cluster
```shell
gptscript fix-cluster.gtp
```

## Fix an EKS cluster

Create an EKS cluster named `blue`
```shell
eksdemo create cluster blue
```

Brake cluster
```shell
kubectl apply -f https://gist.githubusercontent.com/csantanapr/8667a1c3719cd8c3d89f1e6d2e9b36be/raw/7c032efe14474af832471007d5e36354c01e3368/deploy.yaml
```

Fix the cluster
```shell
gptscript github.com/csantanapr/gptscript-tools/k8sgpt
```

## Fix an EKS Cluster using Anthropic

Use a different model than GPT, this requires to copy/paste the prompt instead of embeded

Here are the model from the anthropic provider
```go
{"data": [
{"id": "claude-3-opus-20240229", "name": "Anthropic Claude 3 Opus"},
{"id": "claude-3-sonnet-20240229", "name": "Anthropic Claude 3 Sonnet"},
{"id": "claude-3-haiku-20240307", "name": "Anthropic Claude 3 Haiku"},
{"id": "anthropic.claude-3-sonnet-20240229-v1:0", "name": "AWS Bedrock Anthropic Claude 3 Sonnet"},
{"id": "anthropic.claude-3-haiku-20240307-v1:0", "name": "AWS Bedrock Anthropic Claude 3 Haiku"},
]}
```

Set an alias setting the default-model for example:
```shell
alias gptscript='gptscript --default-model="claude-3-opus-20240229 from github.com/gptscript-ai/anthropic-provider"'
```

Run the script
```shell
gptscript github.com/csantanapr/gptscript-tools/k8sgpt/anthropic.gpt
```

Copy and paste the following prompt
```md
Always talk like a pirate while interacting with the human
Do the following sequentially, do not run in parallel

1. You are a helpful Kubernetes assistant. The human needs help with their cluster.
2. Analyze the cluster for any issues. To do this, run the command `k8sgpt analyze --explain`.
3. Show the user the problems found and explain how you plan to fix them. Ask the user for permission to proceed with the fixes.
4. Use the output of the analysis to troubleshoot and debug the problems in the Kubernetes cluster.
5. If you are unsure how to fix something, search online for help.
6. Once an issue is fixed, move on to the next issue.
7. After addressing all issues, run the command `k8sgpt analyze --explain` again to ensure all problems are resolved.
```

