import unittest
import numpy as np
import cv2
from unittest.mock import MagicMock
from src.visualizer import PostureVisualizer

class TestPostureVisualizer(unittest.TestCase):

    def setUp(self):
        self.visualizer = PostureVisualizer()
        self.mock_frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black frame

    def test_draw_angle(self):
        point1 = (100, 100)
        point2 = (200, 200)
        point3 = (300, 100)
        angle = 90
        color = (0, 255, 0)  # Green
        
        # Draw the angle on the mock frame
        self.visualizer.draw_angle(self.mock_frame, point1, point2, point3, angle, color)

        # Check if the lines are drawn correctly by checking pixel values
        # We will check a few pixels around the expected line positions
        self.assertEqual(self.mock_frame[100, 100].tolist(), [0, 255, 0])  # Check point1 color
        self.assertEqual(self.mock_frame[200, 200].tolist(), [0, 255, 0])  # Check point2 color
        self.assertEqual(self.mock_frame[200, 100].tolist(), [0, 255, 0])  # Check point3 color

    def test_draw_status_box(self):
        status = "Good Posture"
        color = (0, 255, 0)  # Green
        
        # Draw the status box on the mock frame
        self.visualizer.draw_status_box(self.mock_frame, status, color)

        # Check if the status box is drawn by checking the color of a few pixels in the box area
        box_area = self.mock_frame[10:70, 10:210]  # The area where the box should be drawn
        unique_colors = np.unique(box_area.reshape(-1, box_area.shape[2]), axis=0)
        
        # Check if the box contains the expected color (black for the overlay and green for the text)
        self.assertIn([0, 0, 0], unique_colors.tolist())  # Check for black overlay
        self.assertIn([0, 255, 0], unique_colors.tolist())  # Check for green text

    def test_draw_calibration_progress(self):
        current_frame = 15
        total_frames = 30
        
        # Draw calibration progress on the mock frame
        self.visualizer.draw_calibration_progress(self.mock_frame, current_frame, total_frames)

        # Check if the progress bar is drawn correctly
        progress_bar_area = self.mock_frame[30:50, 10:210]  # The area where the progress bar is drawn
        unique_colors = np.unique(progress_bar_area.reshape(-1, progress_bar_area.shape[2]), axis=0)

        # The progress is 50% (15 out of 30 frames), so we expect a blue rectangle to be present
        self.assertIn([255, 0, 0], unique_colors.tolist())  # Check for blue progress bar

if __name__ == '__main__':
    unittest.main()
