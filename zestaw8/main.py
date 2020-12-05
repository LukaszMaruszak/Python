import time
import unittest
import random
from math import sqrt

# zadanie 8.1


def solve(a, b, c):
    """Funkcja szukająca rozwiązanie równania liniowego a * x + b * y + c = 0"""
    if a == 0 and b == 0 and c == 0:
        return "Równanie ma nieskończenie wiele rozwiązań"
    elif a == 0 and b == 0:
        return "Równanie sprzeczne"
    elif a == 0:
        return "y = " + str(-c/b)
    elif b == 0:
        return "x = " + str(-c/a)
    else:
        return "y = -({} * x + {}) / {}".format(a, b, c)

# zadanie 8.3


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    points_in_quarter = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            points_in_quarter += 1
    return "Liczba PI = {} dla {} losowań".format((4 * points_in_quarter / n), n)


print("zadanie 8.3")
print(calc_pi(100))
print(calc_pi(10000))
print(calc_pi(1000000))
print("Wzrost dokładności liczb PI ze wzrostem ilości losowań.")

# zadanie 8.4


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Długość odcinka musi być większa niż 0")
    elif b + c <= a or a + c <= b or a + b <= c:
        raise ValueError("Z tych odcinków nie można zbudować trójkąta")
    else:
        p = (a + b + c) / 2
        pole = sqrt(p * (p - a) * (p - b) * (p - c))
    return round(pole, 2)

# zadanie 8.6


def recursiveP(i, j):
    if i < 0 and j < 0:
        raise ValueError("Podaj liczby nieujemne")

    if i > 0 and j > 0:
        return 0.5 * (recursiveP(i-1, j) + recursiveP(i, j-1))
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5


def dynamicP(i, j):
    wartosciP = {}
    if i < 0 and j < 0:
        raise ValueError("Podaj liczby nieujemne")
    wartosciP[(0, 0)] = 0.5

    for l in range(1, i+1):
        wartosciP[(l, 0)] = 0

    for m in range(1, j+1):
        wartosciP[(0, m)] = 1.0

    for x in range(1, i+1):
        for y in range(1, j+1):
            wartosciP[(x, y)] = 0.5 * (wartosciP[(x-1, y)] + wartosciP[(x, y-1)])

    return wartosciP.get((i, j))


class MyTestCase(unittest.TestCase):

    def test_solveLinear(self):
        self.assertEqual(solve(1, 2, 3), "y = -(1 * x + 2) / 3")
        self.assertEqual(solve(0, 0, 0), "Równanie ma nieskończenie wiele rozwiązań")
        self.assertEqual(solve(0, 0, 3), "Równanie sprzeczne")
        self.assertEqual(solve(0, 2, 3), "y = -1.5")
        self.assertEqual(solve(1, 0, 3), "x = -3.0")

    def test_heron(self):
        self.assertEqual(heron(4, 5, 7), 9.8)
        self.assertEqual(heron(3, 5, 7), 6.5)
        try:
            heron(0, 0, 0)
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)
        try:
            heron(-4, 0, -13)
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)
        try:
            heron(1, 10, 2)
        except Exception as e1:
            self.assertEqual(e1.__class__, ValueError)

    def test_recusriveP(self):
        self.assertEqual(recursiveP(0, 0), 0.5)
        self.assertEqual(recursiveP(0, 1), 1.0)
        self.assertEqual(recursiveP(1, 0), 0.0)
        self.assertEqual(recursiveP(1, 1), 0.5)
        self.assertEqual(recursiveP(1, 2), 0.75)
        self.assertEqual(recursiveP(2, 1), 0.25)
        self.assertEqual(recursiveP(2, 2), 0.5)

    def test_dynamicP(self):
        self.assertEqual(dynamicP(0, 0), 0.5)
        self.assertEqual(dynamicP(0, 1), 1.0)
        self.assertEqual(dynamicP(1, 0), 0.0)
        self.assertEqual(dynamicP(1, 1), 0.5)
        self.assertEqual(dynamicP(1, 2), 0.75)
        self.assertEqual(dynamicP(2, 1), 0.25)
        self.assertEqual(dynamicP(2, 2), 0.5)


if __name__ == '__main__':
    print("\nTeraz wykonuje się funkcja P(14, 14) za chwile poznasz wyniki:")
    start1 = time.time()
    recursiveP(14, 14)
    elapsed1 = time.time() - start1
    start2 = time.time()
    dynamicP(14, 14)
    elapsed2 = time.time() - start2
    print("Czas wykonania funkcji rekurencyjnej P to: " + str(elapsed1))
    print("Czas wykonania funkcji dynamicznej P to: " + str(elapsed2))
    input("Funkcja wykorzystująca programowanie dynamiczne jest o wiele szybsza,"
          "\n ponieważ nie wykonuje tych samych obliczeń wiele razy")
    unittest.main()
