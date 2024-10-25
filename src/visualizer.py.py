"""Module for handling all visualization aspects of the posture detector."""

import cv2
from config import COLORS

class PostureVisualizer:
    def __init__(self):
        self.box_margin = 10
        self.box_height = 60
        self.box_width = 200

    def draw_angle(self, frame, point1, point2, point3, angle, color):
        """
        Draw angle visualization on the frame.
        
        Args:
            frame: Video frame to draw on
            point1, point2, point3: Points forming the angle
            angle: Calculated angle value
            color: BGR color tuple
        """
        cv2.line(frame, point1, point2, color, 2)
        cv2.line(frame, point2, point3, color, 2)

        # Draw angle arc
        radius = 30
        center = point2
        start_angle = np.arctan2(point1[1] - point2[1], point1[0] - point2[0])
        end_angle = np.arctan2(point3[1] - point2[1], point3[0] - point2[0])
        
        if start_angle > end_angle:
            start_angle, end_angle = end_angle, start_angle
        
        cv2.ellipse(frame, center, (radius, radius), 0, 
                    start_angle * 180 / np.pi, 
                    end_angle * 180 / np.pi, color, 2)

        text_position = (point2[0] + 10, point2[1] - 10)
        cv2.putText(frame, f"{int(angle)}°", text_position, 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    def draw_status_box(self, frame, status, color):
        """
        Draw status box with current posture information.
        
        Args:
            frame: Video frame to draw on
            status: Status text to display
            color: BGR color tuple for status
        """
        overlay = frame.copy()
        cv2.rectangle(overlay, 
                     (self.box_margin, self.box_margin), 
                     (self.box_margin + self.box_width, self.box_margin + self.box_height),
                     COLORS['BLACK'], -1)
        cv2.addWeighted(overlay, 0.3, frame, 0.7, 0, frame)
        
        cv2.putText(frame, "Status:", (self.box_margin + 5, self.box_margin + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLORS['WHITE'], 1)
        cv2.putText(frame, status, (self.box_margin + 5, self.box_margin + 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    def draw_calibration_progress(self, frame, current_frame, total_frames):
        """
        Draw calibration progress bar and text.
        
        Args:
            frame: Video frame to draw on
            current_frame: Current calibration frame number
            total_frames: Total number of calibration frames needed
        """
        progress = (current_frame / total_frames) * 100
        cv2.rectangle(frame, (10, 30), (10 + int(progress * 2), 50), COLORS['BLUE'], -1)
        cv2.putText(frame, f"Calibrating... {current_frame}/{total_frames}", 
                   (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS['BLUE'], 2)

    def draw_angle_info(self, frame, angle_info, y_start=80):
        """
        Draw angle information on frame.
        
        Args:
            frame: Video frame to draw on
            angle_info: List of tuples (label, angle, threshold)
            y_start: Starting y-position for drawing
        """
        y_pos = y_start
        for label, angle, threshold in angle_info:
            color = COLORS['GREEN'] if angle >= threshold else COLORS['RED']
            cv2.putText(frame, f"{label}: {angle:.1f}°", (10, y_pos),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            y_pos += 20
