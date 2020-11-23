# zad 6.1
import unittest


class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)

    #def __cmp__(self, other): # Python 2, porównywanie, -1|0|+1
    #    """Porównywanie odcinków czasu."""
    #    return cmp(self.s, other.s)

    # Python 2.7 i Python 3, rich comparisons.
    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    # nadmiarowe
    #def __gt__(self, other):
    #    return self.s > other.s

    # nadmiarowe
    #def __ge__(self, other):
    #    return self.s >= other.s

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s


# Kod testujący moduł.


class TestTime(unittest.TestCase):

    def setUp(self): pass

# test str() i repr()
    def test_print(self):
        self.assertEqual(repr(Time(0)), "Time(0)")
        self.assertEqual(repr(Time(25)), "Time(25)")
        self.assertEqual(repr(Time(158)), "Time(158)")
        self.assertEqual(repr(Time(14567)), "Time(14567)")

        self.assertEqual(str(Time(0)), "00:00:00")
        self.assertEqual(str(Time(534)), "00:08:54")
        self.assertEqual(str(Time(903)), "00:15:03")
        self.assertEqual(str(Time(83423)), "23:10:23")

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(1) == Time(1))
        self.assertFalse(Time(6) == Time(3))
        self.assertTrue(Time(234) != Time(90))
        self.assertFalse(Time(0) != Time(0))
        self.assertTrue(Time(12) < Time(13))
        self.assertFalse(Time(6) < Time(5))
        self.assertTrue(Time(2) <= Time(3))
        self.assertTrue(Time(2) <= Time(2))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertTrue(Time(4) >= Time(4))
        self.assertFalse(Time(2) >= Time(3))

    def test_add(self):   # musi działać porównywanie
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(5) + Time(1), Time(6))
        self.assertEqual(Time(10) + Time(100), Time(110))
        self.assertEqual(Time(0) + Time(2), Time(2))
        self.assertEqual(Time(-1) + Time(2), Time(1))
        self.assertEqual(Time(44) + Time(-11), Time(33))
        self.assertEqual(Time(6000) + Time(500), Time(6500))
        self.assertEqual(Time(0) + Time(0), Time(0))

    def test_int(self):
        self.assertEqual(int(Time(0)), 0)
        self.assertEqual(int(Time(12)), 12)
        self.assertEqual(int(Time(2222)), 2222)
        self.assertEqual(int(Time(-1)), -1)
        self.assertEqual(int(Time(54)), 54)
        self.assertEqual(int(Time(9)), 9)
        self.assertEqual(int(Time()), 0)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()     # wszystkie testy


