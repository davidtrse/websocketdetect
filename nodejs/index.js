const WebSocket = require('ws');
const fs = require('fs');

// Path to the image file to send
const IMAGE_PATH = 'minhavatar.jpg';

// Address of the WebSocket server
const WS_URL = 'ws://faceid.pythera.ai:2086';
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function sendImage(wsUrl, imagePath) {
    // Read the content of the image file
    const imageBuffer = fs.readFileSync(imagePath);
    const encodedString = imageBuffer.toString('base64');

    // Create a WebSocket connection
    const ws = new WebSocket(wsUrl);

    ws.on('open', async () => {
        console.log("Connected to WebSocket server");
        
        // Send base64 image data over WebSocket
        ws.send(encodedString, async (error) => {
            if (error) {
                console.error("Failed to send image:", error);
                ws.close(); // Close the connection in case of an error
            } else {
                console.log("Image sent");
                // Sleep for 5 seconds
                for (let i = 1; i <= 5; i++) {
                    await sleep(1000); // Sleep for 1 second each iteration
                    console.log(`Waiting ${i} seconds...`);
                }
                ws.close(); // Manually close the connection after waiting
            }
        });
    });

    ws.on('message', (response) => {
        console.log("Received response:", response);
    });

    ws.on('error', (error) => {
        console.error("WebSocket error:", error);
        ws.close(); // Close the connection in case of an error
    });

    ws.on('close', () => {
        console.log("WebSocket connection closed");
        console.log("Operation completed successfully");
    });
}

// Use the function and handle the promise
sendImage(WS_URL, IMAGE_PATH)
    