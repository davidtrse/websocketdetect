# import cv2
# import numpy as np
# import websocket
import websockets
import sys
import pickle
import struct ### new code
import asyncio
# from PIL import Image
# from gfn.utils import image as imgutils
import base64
# def on_message(ws, message):
#     print(f"Received message: {message}")

# def on_error(ws, error):
#     print(f"Encountered error: {error}")

# def on_close(ws, close_status_code, close_msg):
#     print("Connection closed")

# def on_open(ws):
#     print("Connection opened")
#     ws.send("Hello, Server!")

# if __name__ == "__main__":
#     ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws",
#                                 on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close)
#     ws.on_open = on_open
#     ws.run_forever()
IMAGE_PATH = 'minhavatar.jpg'

async def hello(uri):
    with open(IMAGE_PATH, 'rb') as image_file:
        # Chuyển nội dung ảnh sang base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    async with websockets.connect(uri) as websocket:
        # cap = cv2.VideoCapture(0)
        while True:
            #
            # ret, frame = cap.read()
            # image = Image.fromarray(frame)
            # b64 = imgutils.to_base64(image)
            await websocket.send(encoded_string)
            #
            data = await websocket.recv()
            
            #
            print(data)
                

asyncio.run(hello('ws://faceid.pythera.ai:2086'))