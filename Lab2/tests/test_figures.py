import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestGeometricFigures(unittest.TestCase):
    def test_rectangle_area(self):
        rect = Rectangle(width=3, height=4, color="blue")
        self.assertEqual(rect.area(), 12)

    def test_circle_area(self):
        circle = Circle(radius=1, color="green")
        self.assertAlmostEqual(circle.area(), 3.141592653589793)

    def test_square_area(self):
        square = Square(side=5, color="red")
        self.assertEqual(square.area(), 25)

    def test_square_is_rectangle(self):
        square = Square(side=2, color="yellow")
        self.assertIsInstance(square, Rectangle)

if __name__ == '__main__':
    unittest.main()

# python -m unittest discover -s tests