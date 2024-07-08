import numpy as np

def generate_audio(gesture):
    # Simple audio generation based on gesture
    if gesture == "Thumbs up":
        frequency = 440  # A4 note
    else:
        frequency = 261.63  # C4 note
    
    duration = 0.5  # seconds
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    audio_data = np.sin(2 * np.pi * frequency * t)
    
    # Normalize to 16-bit range
    audio_data = (audio_data * 32767).astype(np.int16)
    
    return audio_data.tobytes()