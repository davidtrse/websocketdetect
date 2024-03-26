const WebSocket = require('ws');
const fs = require('fs');

// Path to the image file
const IMAGE_PATH = 'minhavatar.jpg';

// WebSocket server URL
const WS_URL = 'ws://faceid.pythera.ai:2086';

// Function to encode file content to base64
function encodeBase64(filePath) {
  const fileContent = fs.readFileSync(filePath);
  return Buffer.from(fileContent).toString('base64');
}

// Function to send image and receive response using WebSocket
async function sendImage(wsUrl, imagePath) {
  const encodedString = encodeBase64(imagePath);

  // Create a new WebSocket connection
  const ws = new WebSocket(wsUrl);

  // Wrap WebSocket events in Promises
  const openPromise = new Promise((resolve) => ws.on('open', resolve));
  const messagePromise = new Promise((resolve, reject) => {
    ws.on('message', (data) => {
      console.log("Received response:", data);
      resolve(data);
    });
    ws.on('error', (err) => {
      console.error("WebSocket error:", err);
      reject(err);
    });
    ws.on('close', (code, reason) => {
      console.log(`WebSocket closed with code: ${code}, reason: ${reason}`);
      reject(new Error('WebSocket closed before message was received'));
    });
  });

  // Wait for the connection to open
  await openPromise;
  console.log("Connected to WebSocket server");

  // Send the base64 encoded image data
  ws.send(encodedString);
  console.log("Image sent");

  // Wait for the response from the server or an error/close event
  await messagePromise;

  // Close the WebSocket connection
  ws.close();
}

// Run the sendImage function
sendImage(WS_URL, IMAGE_PATH)
  .then(() => console.log('Image processing complete'))
  .catch((error) => console.error('An error occurred:', error));
