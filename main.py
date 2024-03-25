import base64
import asyncio
import websockets

# Đường dẫn đến file ảnh cần gửi
IMAGE_PATH = 'minhavatar.jpg'

# Địa chỉ của WebSocket server
WS_URL = 'ws://faceid.pythera.ai:2086'

async def send_image(ws_url, image_path):
    # Mở file ảnh và đọc nội dung
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())

    # Tạo một WebSocket connection và gửi/nhận dữ liệu
    async with websockets.connect(ws_url) as ws:
        print("Connected to WebSocket server")

        # Gửi dữ liệu ảnh base64 qua WebSocket
        await ws.send(encoded_string)
        print("Image sent")

        # Nhận phản hồi từ server
        response = await ws.recv()
        print("Received response:", response)

if __name__ == "__main__":
    # Chạy event loop cho coroutine
    asyncio.get_event_loop().run_until_complete(send_image(WS_URL, IMAGE_PATH))
