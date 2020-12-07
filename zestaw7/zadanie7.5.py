from points import Point
import unittest
import math

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
            return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Błędny drugi argument")
        return not self == other

    def area(self):
        """Obliczenie pola powierzchni koła"""
        return math.pi * self.radius * self.radius

    def move(self, x, y):
        """Przesuniecie o (x, y)"""
        new_x = self.pt.x + x
        new_y = self.pt.y + y
        return Circle(new_x, new_y, self.radius)

    def cover(self, other):
        """Najmniejszy okrąg pokrywający oba"""
        if not isinstance(other, Circle):
            raise ValueError("Musisz podać dwa okręgi")

        if self.pt == other.pt:
            return Circle(self.pt.x, self.pt.y, max(self.radius, other.radius))

        d = math.sqrt((other.pt.x - self.pt.x)**2 + (other.pt.y - self.pt.y)**2)
        if self.radius > (d + other.radius):
            #Drugie koło znajduje się w większym self
            return self

        max_radius = max(self.radius, other.radius)
        new_radius = (math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2))/2
        new_radius = max_radius + new_radius
        n_x = (self.pt.x + other.pt.x) / 2
        n_y = (self.pt.y + other.pt.y) / 2
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
        self.assertAlmostEqual(self.c1.area(), 12.566, places=2)
        self.assertAlmostEqual(self.c2.area(), 78.539, places=2)
        self.assertAlmostEqual(self.c3.area(), 314.16, places=2)

    def test_move(self):
        self.assertEqual(self.c1.move(1, 1), Circle(2, 2, 2))
        self.assertEqual(self.c2.move(2, -2), Circle(2, -2, 5))
        self.assertEqual(self.c3.move(-4, -1), Circle(-5, 1, 10))

    def test_cover(self):
        try:
            self.assertEqual(Circle(0, 0, 3).cover([6, -3, 4]), Circle(2, 1.5, 12.5))
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)

        self.assertEqual(Circle(1, 1, 10).cover(Circle(1, 1, 2)), Circle(1, 1, 10))

        self.assertEqual(Circle(0, 0, 20).cover(Circle(2, 2, 4)), Circle(0, 0, 20))

        self.assertEqual(Circle(5, 5, 5).cover(Circle(0, 0, 5)), Circle(2.5, 2.5, 8.54))

        self.assertEqual(Circle(-2, 2, 4).cover(Circle(-3, -8, 2)), Circle(-2.5, -3.0, 9.02))


if __name__ == '__main__':
    unittest.main()