import unittest
from area import * 

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(a=3, b=4, c=5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_invalid(self):
        with self.assertRaises(ValueError):
            Triangle(a=1, b=2, c=3)

    def test_right_angle_triangle(self):
        triangle = Triangle(a=3, b=4, c=5)
        self.assertTrue(triangle.is_right_angle())

    def test_non_right_angle_triangle(self):
        triangle = Triangle(a=3, b=4, c=6)
        self.assertFalse(triangle.is_right_angle())

    def test_calculate_area_circle(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483)

    def test_calculate_area_triangle(self):
        triangle = Triangle(a=3, b=4, c=5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

if __name__ == '__main__':
    unittest.main()
