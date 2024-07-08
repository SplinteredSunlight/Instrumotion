import mediapipe as mp
import cv2
import logging
from src.config import active_config as config

# Set up logging
logger = logging.getLogger(__name__)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=config.GESTURE_CONFIDENCE_THRESHOLD)

def process_gestures(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Simple gesture recognition based on thumb tip position
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            if thumb_tip.y < index_tip.y:
                logger.debug("Recognized gesture: Thumbs up")
                return "Thumbs up"
            else:
                logger.debug("Recognized gesture: Other gesture")
                return "Other gesture"
    
    logger.debug("No hand detected")
    return "No hand detected"