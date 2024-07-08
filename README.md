# Instrumotion

Instrumotion is an innovative application that transforms hand and body gestures, expression and movements into music using computer vision and machine learning techniques.

## Project Overview

Instrumotion uses real-time hand gesture recognition to generate corresponding audio output. It combines elements of computer vision, real-time web communication, and audio processing to create an interactive, gesture-based musical experience.

## Key Components

1. **Server (src/server.py)**: 
   - Built using FastAPI for handling WebSocket connections and serving static files.
   - Processes incoming video frames from the client.

2. **Gesture Processing (src/gesture_processor.py)**:
   - Utilizes MediaPipe for hand tracking and gesture recognition.
   - Analyzes video frames to detect and interpret hand gestures.

3. **Audio Generation (src/audio_generator.py)**:
   - Generates audio based on recognized gestures.

4. **Web Interface (static/index.html)**:
   - Provides a user interface for the application.
   - Captures video from the user's camera and sends frames to the server.
   - Displays recognized gestures and plays generated audio.

## Project Structure

```
Instrumotion/
├── src/
│   ├── server.py
│   ├── gesture_processor.py
│   ├── audio_generator.py
│   └── config.py
├── static/
│   ├── index.html
│   ├── manifest.json
│   └── favicon_io/
│       └── (favicon files)
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/SplinteredSunlight/Instrumotion.git
   cd Instrumotion
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the server:
   ```
   python src/server.py
   ```

5. Open a web browser and navigate to `http://localhost:8080` to use the application.

## Current Status

- Basic server infrastructure is set up and running.
- WebSocket communication is established.
- Basic gesture recognition is implemented.
- Simple audio generation is in place.
- The web interface can capture and send video frames.

## Next Steps and Potential Improvements

1. Enhance gesture recognition to include more complex gestures.
2. Improve audio generation for more sophisticated and musical sounds.
3. Implement real-time audio playback in the web interface.
4. Add user controls for selecting different instruments or sound types.
5. Implement multi-user functionality for collaborative music creation.
6. Optimize performance for low-latency gesture recognition and audio generation.
7. Enhance the web interface with more interactive elements and visual feedback.
8. Implement comprehensive error handling and logging.

## Contributing

Contributions to Instrumotion are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.