import asyncio
import websockets

from playsound import playsound

class server:
    def __init__(self, port, address):
        self.port = port
        self.address = address

        self.server = websockets.serve(self.main_loop, address, port)

        loop=asyncio.get_event_loop()   
        loop.run_until_complete(self.server)
        loop.run_forever()


    async def main_loop(self, websocket, path):
            msg = await websocket.recv()
            if (msg == "dingdong"):
                playsound("./sfx.mp3")

if __name__ == "__main__":
    server = server(6969,"localhost")

    
    
