"""Configuration settings for the posture detector application."""

# Camera settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# MediaPipe settings
MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5

# Calibration settings
CALIBRATION_FRAMES = 30
ANGLE_THRESHOLD_OFFSET = 10

# Alert settings
ALERT_COOLDOWN = 5  # seconds
SOUND_FILE = "../assets/alert_sound.wav"

# Colors (BGR format)
COLORS = {
    'RED': (0, 0, 255),
    'GREEN': (0, 255, 0),
    'BLUE': (255, 128, 0),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0)
}
