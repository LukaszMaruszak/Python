import unittest
from math import gcd


def add_frac(frac1, frac2):
    val = [frac1[0]*frac2[1] + frac2[0]*frac1[1], frac1[1]*frac2[1]]
    return tearDown(val)


def sub_frac(frac1, frac2):
    val = [frac1[0]*frac2[1] - frac2[0]*frac1[1], frac1[1]*frac2[1]]
    return tearDown(val)


def mul_frac(frac1, frac2):
    val = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return tearDown(val)


def div_frac(frac1, frac2):
    val = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
    return tearDown(val)


def is_positive(frac):
    return True if frac[0] * frac[1] > 0 else False


def is_zero(frac):
    return True if frac[0] == 0 or frac[1] == 1 else False


def cmp_frac(frac1, frac2):
    if sub_frac(frac1, frac2) == [0, 1]:
        return 0
    elif is_positive(sub_frac(frac1, frac2)):
        return 1
    else:
        return -1


def frac2float(frac):
    return frac[0] / frac[1]


def tearDown(frac):
    nwd = gcd(frac[0], frac[1])
    if nwd > 1:
        frac[0] /= nwd
        frac[1] /= nwd
    return frac

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [1, 2]
        self.f2 = [1, 3]
        self.f3 = [5, 6]
        self.f4 = [4, 5]
        self.f5 = [5, 9]
        self.f6 = [11, 45]
        self.f7 = [1, 6]
        self.f8 = [2, 3]


    def test_add_frac(self):
        self.assertEqual(add_frac(self.f1, self.f2), self.f3)

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f4, self.f5), self.f6)

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.f1, self.f2), self.f7)

    def test_div_frac(self):
        self.assertEqual(div_frac(self.f2, self.f1), self.f8)

    def test_is_positive(self):
        self.assertEqual(is_positive(self.f1), True)
        self.assertEqual(is_positive([-1, 3]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([2, 14]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f1, self.f1), 0)
        self.assertEqual(cmp_frac([-10, 2], [10, 2]), -1)
        self.assertEqual(cmp_frac([20, 2], [10, 2]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)

    def tearDown(self):
        self.assertEqual(tearDown([21, 14]), [3, 2])


if __name__ == '__main__':
    unittest.main()
