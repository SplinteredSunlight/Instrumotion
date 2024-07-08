import os

class Config:
    # Common configurations
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    # Server configurations
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8080))

    # Audio configurations
    SAMPLE_RATE = int(os.getenv('SAMPLE_RATE', 44100))
    AUDIO_DURATION = float(os.getenv('AUDIO_DURATION', 0.5))

    # Gesture configurations
    GESTURE_CONFIDENCE_THRESHOLD = float(os.getenv('GESTURE_CONFIDENCE_THRESHOLD', 0.7))

# You can add more environment-specific configurations here if needed
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Set the active configuration based on the INSTRUMOTION_ENV environment variable
active_config = DevelopmentConfig if os.getenv('INSTRUMOTION_ENV') != 'production' else ProductionConfig