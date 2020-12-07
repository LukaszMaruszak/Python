from math import gcd
import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Mianownik nie może być równy 0!")
        else:
            self.x = x
            self.y = y
            nwd = gcd(self.x, self.y)
            if nwd > 1:
                self.x //= nwd
                self.y //= nwd

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
        if isinstance(other, int):
            x = other * self.y
            y = self.y
            return self.x == x and self.y == y

        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            return self.x == x and self.y == y

        if isinstance(other, Frac):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if isinstance(other, int):
            x = other * self.y
            y = self.y
            return self.x != x

        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            return self.x != x and self.y != y

        if isinstance(other, Frac):
            return self.x != other.x and self.y != other.y

    def __lt__(self, other):
        if isinstance(other, int):
            x = other * self.y
            return self.x < x

        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            new_other = Frac(x, y)
            return float(self) < float(new_other)

        if isinstance(other, Frac):
            return float(self) < float(other)

    def __le__(self, other):
        if isinstance(other, int):
            x = other * self.y
            return self.x <= x

        if isinstance(other, float):
            x, y = other.as_integer_ratio()
            new_other = Frac(x, y)
            return float(self) <= float(new_other)

        if isinstance(other, Frac):
            return float(self) <= float(other)

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):
        """frac1 + frac2 frac + int frac + float"""
        if isinstance(other, Frac):
            return Frac(self.x * other.y + self.y * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x + (other*self.y), self.y)
        elif isinstance(other, float):
            new_frac = other.as_integer_ratio()
            other = Frac(new_frac[0], new_frac[1])
            return Frac(self.x * other.y + self.y * other.x, self.y * other.y)
        else:
            raise ValueError("Niewłaściwy argument w dodawaniu")

    __radd__ = __add__  # int+frac

    def __sub__(self, other):
        """frac1 - frac2 frac-int frac-float"""
        if isinstance(other, Frac):
            return Frac(self.x * other.y - self.y * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x - (other * self.y), self.y)
        elif isinstance(other, float):
            new_frac = other.as_integer_ratio()
            other = Frac(new_frac[0], new_frac[1])
            return Frac(self.x * other.y - self.y * other.x, self.y * other.y)
        else:
            raise ValueError("Niewłaściwy argument w odejmowaniu")

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        """frac1 * frac2 frac * int frac-float"""
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x * other, self.y)
        elif isinstance(other, float):
            new_frac = other.as_integer_ratio()
            other = Frac(new_frac[0], new_frac[1])
            return Frac(self.x * other.x, self.y * other.y)
        else:
            raise ValueError("Niewłaściwy argument w mnożeniu")

    __rmul__ = __mul__  # int*frac

    def __truediv__(self, other):
        """frac1 / frac2,   frac / int,   frac / float"""
        if isinstance(other, Frac):
            if other.x == 0 or other.y == 0:
                raise ZeroDivisionError
            else:
                return Frac(self.x * other.y, self.y * other.x)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError
            else:
                return Frac(self.x, self.y * other)
        elif isinstance(other, float):
            if other == 0:
                raise ZeroDivisionError
            else:
                new_frac = other.as_integer_ratio()
                other = Frac(new_frac[0], new_frac[1])
                return Frac(self.x * other.y, self.y * other.x)
        else:
            raise ValueError("Niewłaściwy argument w dzieleniu")

    def __rtruediv__(self, other):
        """int / frac"""
        if self.x == 0 or self.y == 0:
            raise ZeroDivisionError
        else:
            if isinstance(other, int):
                return Frac(self.y * other, self.x)
            else:
                raise ValueError("Niewłaściwy argument w dzieleniu")

    # operatory jednoargumentowe
    def __pos__(self):
        """+frac = (+1)*frac"""
        return self

    def __neg__(self):
        """-frac = (-1)*frac"""
        return Frac((-1) * self.x, self.y)

    def __invert__(self):
        """odwrotnosc: ~frac"""
        return Frac(self.y, self.x)

    def __float__(self):
        """float(frac)"""
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # assert set([2]) == set([2.0])


# Kod testujący moduł.


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = Frac(0, 1)
        self.f12 = Frac(1, 2)
        self.f13 = Frac(1, 3)
        self.f34 = Frac(3, 4)
        self.f56 = Frac(5, 6)
        self.f45 = Frac(4, 5)
        self.f59 = Frac(5, 9)
        self.f1145 = Frac(11, 45)
        self.f16 = Frac(1, 6)
        self.f23 = Frac(2, 3)

    # test str() i repr()
    def test_print(self):
        self.assertEqual(repr(Frac(0, 1)), "Frac(0, 1)")

        # Rozwiązany problem niejednoznaczności zera, tylko Frac(0, 1) to zero
        self.assertEqual(repr(Frac(2, 3)), "Frac(2, 3)")
        self.assertEqual(repr(Frac(-4, 6)), "Frac(-2, 3)")

        self.assertEqual(str(Frac(56, 1)), "56")
        self.assertEqual(str(Frac(4, 9)), "4/9")
        self.assertEqual(str(Frac(-2, 10)), "-1/5")
        self.assertEqual(str(Frac(4, 6)), "2/3")

    def test_add(self):
        self.assertEqual(self.f12 + self.f12, Frac(1, 1))
        self.assertEqual(Frac(1, 2) + Frac(1, 2), Frac(1))
        self.assertEqual(self.f56 + self.f13, Frac(7, 6))
        self.assertEqual(Frac(-4, 6) + Frac(2, 4), Frac(-1, 6))
        self.assertEqual(Frac(4, 6) + Frac(-2, 4), Frac(1, 6))

        self.assertEqual(Frac(1, 2) + 5, Frac(11, 2))
        self.assertEqual(5 + Frac(1, 2), Frac(11, 2))

        self.assertEqual(Frac(1, 4) + 1.5, Frac(7, 4))
        self.assertEqual(1.5 + Frac(1, 4), Frac(7, 4))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 2), Frac(0, 1))
        self.assertEqual(Frac(2, 4) - Frac(1, 4), Frac(1, 4))
        self.assertEqual(Frac(3, 9) - Frac(2, 7), Frac(1, 21))
        self.assertEqual(Frac(4, 6) - Frac(-2, 4), Frac(7, 6))
        self.assertEqual(Frac(-1, 2) - Frac(2, 5), Frac(-9, 10))

        self.assertEqual(Frac(4, 6) - 2, Frac(-8, 6))
        self.assertEqual(2 - Frac(4, 6), Frac(8, 6))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(1, 2) * Frac(0, 1), Frac(0, 1))
        self.assertEqual(Frac(-2, 6) * Frac(2, 3), Frac(-4, 18))
        self.assertEqual(Frac(-2, 6) * Frac(2, 3), Frac(-4, 18))
        self.assertEqual(Frac(2, 6) * Frac(-2, 3), Frac(-4, 18))

        self.assertEqual(Frac(2, 6) * 2, Frac(4, 6))
        self.assertEqual(-3 * Frac(1, 7), Frac(-3, 7))

        self.assertEqual(Frac(1, 2) * 0.5, Frac(1, 4))
        self.assertEqual(0.5 * Frac(1, 2), Frac(1, 4))

    def test_div(self):
        self.assertEqual(Frac(5, 6) / Frac(2, 4), Frac(5, 3))
        self.assertEqual(Frac(-5, 6) / Frac(2, 4), Frac(-5, 3))
        self.assertEqual(Frac(-5, 6) / Frac(2, 4), Frac(-5, 3))
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) / Frac(0, 1)

        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) / 0

        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) / 0.0

        self.assertEqual(Frac(5, 6) / 2, Frac(5, 12))
        self.assertEqual(Frac(5, 6) / 2.5, Frac(1, 3))

        self.assertEqual(2 / self.f45, Frac(10, 4))

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Frac(1, 1) == Frac(1, 1))
        self.assertFalse(Frac(1, 10) == Frac(0, 1))
        self.assertFalse(Frac(1, 10) == 6)
        self.assertTrue(Frac(10, 10) == 1)
        self.assertFalse(Frac(1, 6) == 1.5)
        self.assertTrue(Frac(1, 2) == 0.5)
        self.assertTrue(Frac(2, 3) != Frac(3, 2))
        self.assertFalse(Frac(1, 2) != Frac(1, 2))
        self.assertTrue(Frac(3, 5) < Frac(4, 5))
        self.assertFalse(Frac(8, 9) < Frac(7, 9))
        self.assertFalse(Frac(8, 9) <= 0.1)
        self.assertTrue(Frac(1, 2) < 5)
        self.assertTrue(Frac(1, 2) < 5.8)
        self.assertTrue(5.8 > Frac(1, 2))
        self.assertTrue(5.8 >= Frac(1, 2))
        self.assertTrue(6 >= Frac(1, 2))
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
        self.assertEqual(+(Frac(-4, 5)), Frac(-4, 5))
        self.assertEqual(+(Frac(1, -9)), Frac(1, -9))

    def test_neg(self):
        self.assertEqual(-(Frac(1, 2)), Frac(-1, 2))
        self.assertEqual(-(Frac(-4, 6)), Frac(4, 6))
        self.assertEqual(-(Frac(1, -9)), Frac(-1, -9))

    def test_invert(self):
        self.assertEqual(~(Frac(2, 5)), Frac(5, 2))
        self.assertEqual(~(Frac(-2, 3)), Frac(3, -2))

    def test_float(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(Frac(-3, 5)), -0.6)
        self.assertEqual(float(Frac(7, -10)), -0.7)
        self.assertEqual(float(Frac(0, 1)), 0.0)

    def test_hash(self):
        self.assertEqual(self.f12.__hash__(), hash(0.5))
        self.assertEqual(self.f34.__hash__(), hash(0.75))


if __name__ == '__main__':
    unittest.main()
