import base64
import websocket

# Đường dẫn đến file ảnh cần gửi
IMAGE_PATH = 'minhavatar.jpg'

# Địa chỉ của WebSocket server
WS_URL = 'ws://faceid.pythera.ai:2086'

def send_image(ws_url, image_path):
    # Mở file ảnh và đọc nội dung
    with open(image_path, 'rb') as image_file:
        # Chuyển nội dung ảnh sang base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # Tạo một WebSocket connection
    ws = websocket.WebSocket()
    try:
        ws.connect(ws_url)
        print("Connected to WebSocket server")

        # Gửi dữ liệu ảnh base64 qua WebSocket
        ws.send(encoded_string)
        print("Image sent")

        # Nhận phản hồi từ server
        response = ws.recv()
        print("Received response:", response)

    except Exception as e:
        print("Error:", e)
    finally:
        # Đóng WebSocket connection
        ws.close()

if __name__ == "__main__":
    send_image(WS_URL, IMAGE_PATH)
