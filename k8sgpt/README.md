## Fix a Kubernetes Cluster

You can create a cluster with `kind` or `eksdemo`

Create a kind cluster:
```shell
kind create cluster
```

Create an EKS cluster named `blue`
```shell
eksdemo create cluster blue
```

Brake cluster
```shell
kubectl apply -f brake-cluster.gpt
```

Fix cluster (like a pirate)
```shell
gptscript fix-cluster.gtp
```

## Fix an EKS Cluster using Anthropic

Use a different model than GPT, this requires to copy/paste the prompt instead of embeded

Here are the model from the anthropic provider
```go
    if type(client) == AsyncAnthropic:
        data = [{"id": "claude-3-opus-20240229", "name": "Anthropic Claude 3 Opus"},
                {"id": "claude-3-sonnet-20240229", "name": "Anthropic Claude 3 Sonnet"},
                {"id": "claude-3-haiku-20240307", "name": "Anthropic Claude 3 Haiku"},
                {"id": "claude-3-5-sonnet-20240620", "name": "Anthropic Claude 3.5 Sonnet"}, ]
    else:
        data = [{"id": "anthropic.claude-3-opus-20240229-v1:0", "name": "AWS Bedrock Anthropic Claude 3 Opus"},
                {"id": "anthropic.claude-3-sonnet-20240229-v1:0", "name": "AWS Bedrock Anthropic Claude 3 Sonnet"},
                {"id": "anthropic.claude-3-haiku-20240307-v1:0", "name": "AWS Bedrock Anthropic Claude 3 Haiku"},
                {"id": "anthropic.claude-3-5-sonnet-20240620-v1:0",
                 "name": "AWS Bedrock Anthropic Claude 3.5 Sonnet"}, ]
```
For more info check [here](https://github.com/gptscript-ai/claude3-provider-common/blob/main/claude3_provider_common/main.py#L17-L29)

Set an alias setting the default-model for example:
```shell
alias ai='../../gptscript/bin/gptscript --default-model="claude-3-5-sonnet-20240620 from github.com/gptscript-ai/anthropic-provider"'
```

Run it
```shell
ai --workspace $PWD/workspace tool.gpt
```
