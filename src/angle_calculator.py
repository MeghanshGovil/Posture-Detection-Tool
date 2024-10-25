"""Module for calculating angles between body landmarks."""

import numpy as np

class AngleCalculator:
    @staticmethod
    def calculate_angle(point1, point2, point3):
        """
        Calculate the angle between three points.
        
        Args:
            point1 (tuple): First point coordinates (x, y)
            point2 (tuple): Second point coordinates (x, y) - vertex of the angle
            point3 (tuple): Third point coordinates (x, y)
            
        Returns:
            float: Angle in degrees
        """
        a = np.array(point1)
        b = np.array(point2)
        c = np.array(point3)

        ab = b - a
        bc = c - b
        angle = np.arctan2(bc[1], bc[0]) - np.arctan2(ab[1], ab[0])
        angle = np.abs(angle) * (180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle
