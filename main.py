from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


app = FastAPI()


html = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Страница сообщений</title>
    </head>
    <body>
        <h1>Страница сообщений</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete"=off"/>
            <button>Отправить</button>
        </form>
        <p id='messages'>
        </p>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('p')
                var text = JSON.parse(event.data)
                var content = document.createTextNode(text)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                var json = JSON.stringify(input.value)
                ws.send(json) 
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
'''


@app.get('/')
async def page():
   return HTMLResponse(html)


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    number = 0
    while True:
        data = await websocket.receive_json()
        number += 1
        data = str(number) + '. ' + data
        await websocket.send_json(data)
