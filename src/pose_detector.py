"""Module for handling pose detection and tracking."""

import mediapipe as mp
import numpy as np
from config import MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE

class PoseDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_landmarks(self, frame):
        """
        Detect pose landmarks in a frame.
        
        Args:
            frame: RGB video frame
            
        Returns:
            landmarks: Detected pose landmarks
        """
        results = self.pose.process(frame)
        return results.pose_landmarks if results.pose_landmarks else None

    def draw_landmarks(self, frame, landmarks):
        """
        Draw pose landmarks on frame.
        
        Args:
            frame: Video frame to draw on
            landmarks: Detected pose landmarks
        """
        self.mp_drawing.draw_landmarks(
            frame,
            landmarks,
            self.mp_pose.POSE_CONNECTIONS
        )

    def get_landmark_coordinates(self, landmarks, frame_shape, landmark_index):
        """
        Get coordinates for a specific landmark.
        
        Args:
            landmarks: Detected pose landmarks
            frame_shape: Shape of the video frame
            landmark_index: Index of the desired landmark
            
        Returns:
            tuple: (x, y) coordinates of the landmark
        """
        landmark = landmarks.landmark[landmark_index]
        return (
            int(landmark.x * frame_shape[1]),
            int(landmark.y * frame_shape[0])
        )
