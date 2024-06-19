import json
import os
import yaml
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse

debug: bool = os.environ.get("GPTSCRIPT_DEBUG", "false") == "true"
app = FastAPI()


def log(*args):
    if debug:
        print(args[0])
        if len(args) > 1 and isinstance(args[1], bytes) and args[1].startswith(b"{"):
            json_str = json.dumps(json.loads(args[1]), indent=4, sort_keys=True)
            colored_json = highlight(json_str, JsonLexer(), TerminalFormatter())
            print(colored_json)


@app.middleware("http")
async def log_body(request: Request, call_next):
    body = await request.body()
    log("HTTP REQUEST BODY: ", body)
    return await call_next(request)


@app.post("/")
async def post_root():
    return 'ok'


@app.get("/")
async def get_root():
    return 'ok'


@app.get("/v1/models")
async def list_models() -> JSONResponse:
# read the file models.yaml and return the list of model ids
    with open('models.yaml', 'r') as f:
        data = yaml.safe_load(f)
        # cast the values to str
        models = [{"id": str(item["id"]), "name": str(item["name"])} for item in data["models"]]
        models2 = [{"id": "anthropi.claude-3-haiku-20240307-v1:0", "name":"Claude 3 Haiku"}]

    # pretty print json models
    print(json.dumps(models, indent=2))
    return JSONResponse(content={"data": models})


@app.post("/v1/chat/completions")
async def completions(request: Request) -> StreamingResponse:
    data = await request.body()
    input = json.loads(data)
    # append to input.model the string ":0"
    input["model"] += ":0"
    emulate = {
        "role": "assistant",
        "content": [
      {
        "text": "Hello, world!"
      }
    ]
    }
    # print emulate as json
    print(json.dumps(emulate, indent=2))
    resp = "data: " + json.dumps(emulate) + "\n\n"
    print(resp)
    return StreamingResponse(resp, media_type="application/x-ndjson")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=int(os.environ.get("PORT", "8000")),
                log_level="debug" if debug else "critical", reload=debug, access_log=debug)
