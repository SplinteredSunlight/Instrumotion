from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
import base64
from gesture_processor import process_gestures
from audio_generator import generate_audio
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Instrumotion server is running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("WebSocket connection established")
    while True:
        try:
            data = await websocket.receive_text()
            logger.info("Received frame data")
            # Decode base64 image
            img_data = base64.b64decode(data.split(',')[1])
            nparr = np.frombuffer(img_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            gestures = process_gestures(frame)
            logger.info(f"Recognized gesture: {gestures}")
            audio = generate_audio(gestures)
            
            # For now, just send back the recognized gestures
            await websocket.send_text(f"Recognized gestures: {gestures}")
        except Exception as e:
            logger.error(f"Error in WebSocket connection: {str(e)}")
            break

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Instrumotion server on port 8080")
    uvicorn.run(app, host="0.0.0.0", port=8080)