import numpy as np
import logging
from src.config import active_config as config

# Set up logging
logger = logging.getLogger(__name__)

def generate_audio(gesture):
    logger.debug(f"Generating audio for gesture: {gesture}")
    
    # Simple audio generation based on gesture
    if gesture == "Thumbs up":
        frequency = 440  # A4 note
    else:
        frequency = 261.63  # C4 note
    
    t = np.linspace(0, config.AUDIO_DURATION, int(config.SAMPLE_RATE * config.AUDIO_DURATION), False)
    audio_data = np.sin(2 * np.pi * frequency * t)
    
    # Normalize to 16-bit range
    audio_data = (audio_data * 32767).astype(np.int16)
    
    logger.debug(f"Audio generated with frequency {frequency} Hz")
    return audio_data.tobytes()