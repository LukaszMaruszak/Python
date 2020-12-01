from points import Point
import unittest
from math import sqrt

PI = 3.14


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        """Circle(x, y, radius)"""
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Nie można porównać okręgu z czymś innym niż okrąg")
        else:
            return self.pt.x == other.pt.x and self.pt.y == other.pt.y and self.radius == other.radius

    def __ne__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Błędny drugi argument")
        return not self == other

    def area(self):
        """Obliczenie pola powierzchni koła"""
        return PI * self.radius * self.radius

    def move(self, x, y):
        """Przesuniecie o (x, y)"""
        self.pt.x += x
        self.pt.y += y
        return Circle(self.pt.x, self.pt.y, self.radius)

    def cover(self, other):
        """Najmniejszy okrąg pokrywający oba"""
        if not isinstance(other, Circle):
            raise ValueError("Musisz podać dwa okręgi")
        else:
            max_radius = max(self.radius, other.radius)
            new_radius = (sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2))/2
            new_radius = max_radius + new_radius
            n_x = (abs(self.pt.x - other.pt.x)) / 2
            n_y = (abs(self.pt.y - other.pt.y)) / 2
            return Circle(n_x, n_y, round(new_radius, 2))


# Kod testujący moduł.


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(1, 1, 2)
        self.c2 = Circle(0, 0, 5)
        self.c3 = Circle(-1, 2, 10)
        try:
            self.c4 = Circle(1, 1, -3)
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(1, 1, 2)")
        self.assertEqual(repr(self.c3), "Circle(-1, 2, 10)")
        self.assertEqual(repr(Circle(3, 4, 3)), "Circle(3, 4, 3)")

    def test_equal(self):
        self.assertFalse(self.c1 == self.c2)
        self.assertFalse(Circle(1, 2, 3) == Circle(3, 2, 1))
        self.assertTrue(self.c1 == Circle(1, 1, 2))
        self.assertTrue(Circle(1, 1, 4) == Circle(1, 1, 4))

        try:
            self.assertTrue(Circle(1, 1, 4) == "koło")
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)

        try:
            self.assertTrue(Circle(1, 6, 9) != "koło")
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)

    def test_area(self):
        self.assertEqual(self.c1.area(), 12.56)
        self.assertEqual(self.c2.area(), 78.5)
        self.assertEqual(self.c3.area(), 314)

    def test_move(self):
        self.assertEqual(self.c1.move(1, 1), Circle(2, 2, 2))
        self.assertEqual(self.c2.move(2, -2), Circle(2, -2, 5))
        self.assertEqual(self.c3.move(-4, -1), Circle(-5, 1, 10))

    def test_cover(self):
        try:
            self.assertEqual(Circle(0, 0, 10).cover([1, 2, 10]), Circle(2, 1.5, 12.5))
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)

        self.assertEqual(Circle(0, 0, 10).cover(Circle(4, 3, 2)), Circle(2, 1.5, 12.5))
        self.assertEqual(Circle(2, 2, 4).cover(Circle(3, 8, 2)), Circle(0.5, 3, 7.04))
        self.assertEqual(Circle(-2, 2, 4).cover(Circle(-3, -8, 2)), Circle(0.5, 5, 9.02))


if __name__ == '__main__':
    unittest.main()