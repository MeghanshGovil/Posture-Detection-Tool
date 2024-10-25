"""Main entry point for the posture detector application."""

import cv2
import numpy as np
import time
from playsound import playsound
import os

from config import *
from pose_detector import PoseDetector
from angle_calculator import AngleCalculator
from visualizer import PostureVisualizer

def main():
    # Initialize components
    cap = cv2.VideoCapture(CAMERA_INDEX)
    pose_detector = PoseDetector()
    angle_calculator = AngleCalculator()
    visualizer = PostureVisualizer()

    # Initialize calibration variables
    calibration_data = {
        'left_shoulder': [],
        'right_shoulder': [],
        'neck': [],
        'frames': 0,
        'is_calibrated': False,
        'thresholds': {}
    }
    
    last_alert_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Process frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        landmarks = pose_detector.detect_landmarks(rgb_frame)

        if landmarks:
            # Get key landmarks
            left_shoulder = pose_detector.get_landmark_coordinates(
                landmarks, frame.shape, 
                pose_detector.mp_pose.PoseLandmark.LEFT_SHOULDER.value
            )
            # ... [similar for other landmarks]

            # Calculate angles
            angles = calculate_posture_angles(
                angle_calculator, 
                left_shoulder, right_shoulder, 
                left_ear, right_ear
            )

            # Handle calibration or posture detection
            if not calibration_data['is_calibrated']:
                handle_calibration(frame, calibration_data, angles, visualizer)
            else:
                handle_posture_detection(
                    frame, angles, calibration_data['thresholds'],
                    last_alert_time, visualizer
                )

            # Draw skeleton
            pose_detector.draw_landmarks(frame, landmarks)

        cv2.imshow('Posture Corrector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
