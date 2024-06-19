# Amazon Bedrock Provider for

## Usage Example

```shell
gptscript \
  --default-model='anthropic.claude-3-haiku-20240307-v1:0 from github.com/csantanapr/gptscript-tools/amazon-bedrock-provider' \
  github.com/gptscript-ai/gptscript/examples/helloworld.gpt
```

- See [Amazon Bedrock Supported models and model features](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features) to see which ones support Tool use

- See the [Amazon Bedrock model IDs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html) to get the id read [models.yaml](./models.py)


## Development

* You need to have AWS credentials and a region configured in your environment.

Run using the following commands

```shell
python -m venv .venv
source ./.venv/bin/activate
pip install --upgrade -r requirements.txt
./run.sh
```

```shell
export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export GPTSCRIPT_DEBUG=true
export GPTSCRIPT_JSON_LOG_SINGLE_LINE=true

gptscript --disable-cache --default-model=anthropic.claude-3-sonnet-20240229-v1:0 github.com/gptscript-ai/gptscript/examples/helloworld.gpt
```
