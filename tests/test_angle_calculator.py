import unittest
from src.angle_calculator import AngleCalculator

class TestAngleCalculator(unittest.TestCase):
    
    def test_calculate_angle(self):
        point1 = (0, 0)
        point2 = (1, 1)
        point3 = (2, 0)
        
        angle = AngleCalculator.calculate_angle(point1, point2, point3)
        
        self.assertAlmostEqual(angle, 45.0, places=1)

    def test_calculate_angle_straight_line(self):
        point1 = (0, 0)
        point2 = (1, 1)
        point3 = (1, 2)
        
        angle = AngleCalculator.calculate_angle(point1, point2, point3)
        
        self.assertAlmostEqual(angle, 90.0, places=1)

    def test_calculate_angle_obtuse(self):
        point1 = (0, 0)
        point2 = (1, 1)
        point3 = (0, 2)
        
        angle = AngleCalculator.calculate_angle(point1, point2, point3)
        
        self.assertAlmostEqual(angle, 135.0, places=1)

if __name__ == '__main__':
    unittest.main()
