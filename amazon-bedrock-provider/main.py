import os
import json
import api

from fastapi import Request, Response

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

debug: bool = os.environ.get("GPTSCRIPT_DEBUG", "false") == "true"

app = api.app

def log(*args):
    if debug:
        print(args[0])
        if len(args) > 1 and isinstance(args[1], bytes) and args[1].startswith(b"{"):
            json_str = json.dumps(json.loads(args[1]), indent=4, sort_keys=True)
            colored_json = highlight(json_str, JsonLexer(), TerminalFormatter())
            print(colored_json)

def transform_input(body: bytes) -> bytes:
    data = json.loads(body)
    messages = data.get("messages", [])
    if len(messages) > 0:
        """
        check all messages role with messages[i].get("role")
        If there is no messages with role append {"role": "user", "content": "."}
        """
        for i in range(len(messages)):
            if messages[i].get("role") == "user":
                break
        else:
            messages.append({"role": "user", "content": "."})


    data["messages"] = messages
    #data["stream"] = False
    return json.dumps(data).encode("utf-8")

@app.middleware("http")
async def log_body(request: Request, call_next):
    body = await request.body()
    log("HTTP REQUEST BODY: ", body)
    # if request.scope type is http, method POST, and path `/v1/chat/completions` then call function transform_input
    if request.scope.get("type") == "http" and request.scope.get("method") == "POST" and request.scope.get("path") == "/v1/chat/completions":
        request._body = transform_input(body)
    log("HTTP REQUEST BODY TRANSFORM: ", await request.body())


    # Call the next middleware or route handler
    response = await call_next(request)

    # Log the response body
    response_body = b""
    async for chunk in response.body_iterator:
        # parse chunk replace the string "index":-1 with "index":0
        # chunk = chunk.replace(b'"index":-1', b'"index":0')
        response_body += chunk
    print(f"Response body: {response_body.decode()}")

    # Return the modified response
    return Response(response_body,
                    status_code=response.status_code,
                    headers=dict(response.headers),
                    media_type=response.media_type)







if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=int(os.environ.get("PORT", "8000")),
                log_level="debug" if debug else "critical", reload=debug, access_log=debug)
