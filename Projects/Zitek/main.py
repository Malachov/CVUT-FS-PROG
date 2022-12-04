from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from random import randint
import asyncio
from starlette.endpoints import WebSocketEndpoint

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return "Hello, " + name


@app.get("/UI", response_class=HTMLResponse)
async def load_UI(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         if isinstance(data, str):
#             print("str")
#             # await websocket.send_text(f"{data}")
#             data = '{"axes": [{"name":"A1", "pos":111},{"name":"A2", "pos":222},{"name":"A3", "pos":333},{"name":"A4", "pos":444},{"name":"A5", "pos":555}]}'
#             await websocket.send_text(data)
#             time.sleep(20)
#         else:
#             data = '{"axes": [{"name":"A1", "pos":' + str(randint(0, 10)) + '},{"name":"A2", "pos":' + str(randint(0, 10)) + '},{"name":"A3", "pos":' + str(randint(0, 10)) + '},{"name":"A4", "pos":' + str(randint(0, 10)) + '},{"name":"A5", "pos":' + str(randint(0, 10)) + "}]}"
#             await websocket.send_text(data)
#         time.sleep(1)


@app.websocket_route("/ws")
class WebSocketClass(WebSocketEndpoint):
    async def on_receive(self, websocket, data):
        # ...
        await websocket.send_text(data)

    async def on_connect(self, websocket):
        await websocket.accept()
        asyncio.create_task(self.send_periodically(websocket))

    async def send_periodically(self, websocket):
        while True:
            data = '{"axes": [{"name":"A1", "pos":' + str(randint(0, 10)) + '},{"name":"A2", "pos":' + str(randint(0, 10)) + '},{"name":"A3", "pos":' + str(randint(0, 10)) + '},{"name":"A4", "pos":' + str(randint(0, 10)) + '},{"name":"A5", "pos":' + str(randint(0, 10)) + "}]}"
            await websocket.send_text(data)
            await asyncio.sleep(0.4)
