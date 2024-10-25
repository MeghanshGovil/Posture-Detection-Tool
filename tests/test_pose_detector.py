import unittest
from unittest.mock import MagicMock
from src.pose_detector import PoseDetector

class TestPoseDetector(unittest.TestCase):

    def setUp(self):
        self.pose_detector = PoseDetector()
        self.mock_frame = MagicMock()

    def test_detect_landmarks(self):
        # Simulate the behavior of the pose detection
        self.pose_detector.pose.process = MagicMock(return_value=MagicMock(pose_landmarks=True))
        landmarks = self.pose_detector.detect_landmarks(self.mock_frame)
        self.assertIsNotNone(landmarks)

    def test_get_landmark_coordinates(self):
        # Simulate a mock landmark for testing
        mock_landmarks = MagicMock()
        mock_landmarks.landmark = [MagicMock(x=0.5, y=0.5)]  # Mock a single landmark at (0.5, 0.5)
        frame_shape = (480, 640, 3)  # Mock frame shape
        
        coordinates = self.pose_detector.get_landmark_coordinates(mock_landmarks, frame_shape, 0)
        self.assertEqual(coordinates, (320, 240))  # Expecting (0.5 * 640, 0.5 * 480)

if __name__ == '__main__':
    unittest.main()
