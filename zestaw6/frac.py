from math import gcd
import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y != 0:
            self.x = x
            self.y = y
            nwd = gcd(self.x, self.y)
            if nwd > 1:
                self.x //= nwd
                self.y //= nwd
        else:
            self.x = 0
            self.y = 1

    def __str__(self):
        """Zwraca "x/y" lub "x" dla y=1"""
        if self.y == 1:
            return "{}".format(self.x)
        else:
            return "{}/{}".format(self.x, self.y)

    def __repr__(self):
        """Zwraca "Frac(x, y)"""
        return "Frac({}, {})".format(self.x, self.y)

    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):
        """frac1 + frac2"""
        return Frac(self.x * other.y + self.y * other.x, self.y * other.y)

    def __sub__(self, other):
        """frac1 - frac2"""
        return Frac(self.x * other.y - self.y * other.x, self.y * other.y)

    def __mul__(self, other):
        """frac1 * frac2"""
        return Frac(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        """frac1 / frac2"""
        if other.x == 0:
            raise ZeroDivisionError
        else:
            return Frac(self.x * other.y, self.y * other.x)

    # operatory jednoargumentowe
    def __pos__(self):
        """+frac = (+1)*frac"""
        if self.x < 0:
            self.x *= -1
        return self

    def __neg__(self):
        """-frac = (-1)*frac"""
        return Frac(-self.x, self.y)

    def __invert__(self):
        """odwrotnosc: ~frac"""
        if self < 0:
            #Odwracam ułamek ale - zostaje w liczniku
            self.x, self.y = -1 * self.y, -1 *self.x
            return self
        else:
            return Frac(self.y, self.x)

    def __float__(self):
        """float(frac)"""
        return self.x / self.y



# Kod testujący moduł.


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [1, 2]

    # test str() i repr()
    def test_print(self):
        self.assertEqual(repr(Frac(0, 1)), "Frac(0, 1)")

        # Rozwiązany problem niejednoznaczności zera, tylko Frac(0, 1) to zero
        self.assertEqual(repr(Frac(1, 0)), "Frac(0, 1)")
        self.assertEqual(repr(Frac(2, 3)), "Frac(2, 3)")
        self.assertEqual(repr(Frac(4, 6)), "Frac(2, 3)")

        self.assertEqual(str(Frac(0, 1)), "0")
        self.assertEqual(str(Frac(56, 1)), "56")
        self.assertEqual(str(Frac(4, 9)), "4/9")
        self.assertEqual(str(Frac(-2, 10)), "-1/5")
        self.assertEqual(str(Frac(4, 6)), "2/3")

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1,2), Frac(1, 1))
        self.assertEqual(Frac(1, 2) + Frac(1,2), Frac(1))
        self.assertEqual(Frac(5, 6) + Frac(1, 3), Frac(7, 6))
        self.assertEqual(Frac(-4, 6) + Frac(2, 4), Frac(-1, 6))
        self.assertEqual(Frac(4, 6) + Frac(-2, 4), Frac(1, 6))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 2), Frac(0, 1))
        self.assertEqual(Frac(2, 4) - Frac(1, 4), Frac(1, 4))
        self.assertEqual(Frac(3, 9) - Frac(2, 7), Frac(1, 21))
        self.assertEqual(Frac(4, 6) - Frac(-2, 4), Frac(7, 6))
        self.assertEqual(Frac(-1, 2) - Frac(2, 5), Frac(-9, 10))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(1, 2) * Frac(0, 1), Frac(0, 1))
        self.assertEqual(Frac(-2, 6) * Frac(2, 3), Frac(-4, 18))
        self.assertEqual(Frac(-2, 6) * Frac(2, 3), Frac(-4, 18))
        self.assertEqual(Frac(2, 6) * Frac(-2, 3), Frac(-4, 18))

    def test_div(self):
        self.assertEqual(Frac(5, 6) / Frac(2, 4), Frac(5, 3))
        self.assertEqual(Frac(-5, 6) / Frac(2, 4), Frac(-5, 3))
        self.assertEqual(Frac(-5, 6) / Frac(2, 4), Frac(-5, 3))
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) / Frac(0, 1)

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Frac(1, 1) == Frac(1, 1))
        self.assertFalse(Frac(1, 10) == Frac(0, 1))
        self.assertTrue(Frac(2, 3) != Frac(3, 2))
        self.assertFalse(Frac(1, 2) != Frac(1, 2))
        self.assertTrue(Frac(3, 5) < Frac(4, 5))
        self.assertFalse(Frac(8, 9) < Frac(7, 9))
        self.assertTrue(Frac(2, 4) <= Frac(3, 4))
        self.assertTrue(Frac(2, 5) <= Frac(2, 5))
        self.assertFalse(Frac(4, 6) <= Frac(3, 6))
        self.assertTrue(Frac(4, 8) > Frac(1, 9))
        self.assertFalse(Frac(1, 10) > Frac(3, 6))
        self.assertTrue(Frac(2, 3) >= Frac(3, 6))
        self.assertTrue(Frac(4, 7) >= Frac(4, 7))
        self.assertFalse(Frac(1, 7) >= Frac(3, 2))

    def test_pos(self):
        self.assertEqual(+(Frac(1, 2)), Frac(1, 2))
        self.assertEqual(+(Frac(-12, 22)), Frac(12, 22))

    def test_neg(self):
        self.assertEqual(-(Frac(1, 2)), Frac(-1, 2))
        self.assertEqual(-(Frac(-4, 6)), Frac(4, 6))

    def test_invert(self):
        self.assertEqual(~(Frac(2, 5)), Frac(5, 2))
        self.assertEqual(~(Frac(-2, 3)), Frac(-3, 2))

    def test_float(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(Frac(-3, 5)), -0.6)
        self.assertEqual(float(Frac(7, -10)), -0.7)
        self.assertEqual(float(Frac(0, 1)), 0.0)


if __name__ == '__main__':
    unittest.main()
