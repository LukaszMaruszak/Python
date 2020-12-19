import unittest
import random


class RandomQueue:

    def __init__(self):
        self.item = []

    def insert(self, item):
        self.item.append(item)

    def remove(self):  # zwraca losowy element
        if self.is_empty():
            raise IndexError("Kolejka jest pusta, nie można usunąć")
        dlugoscKolejki = len(self.item)
        x = random.randint(0, dlugoscKolejki-1)

        # pop jest O(1) ale tylko jak usuwa ostatni element dlatego muszę zaminić miejscami
        self.item[dlugoscKolejki-1], self.item[x] = self.item[x], self.item[dlugoscKolejki-1]
        return self.item.pop()

    def is_empty(self):
        return len(self.item) == 0

    def is_full(self):
        return False

    def clear(self):
        self.item = []  # czyszczenie listy

class TestRandomQueue(unittest.TestCase):

    def setUp(self):
        self.randomqueue = RandomQueue()

    def test_is_empty(self):
        self.assertTrue(self.randomqueue.is_empty())

    def test_put(self):
        self.randomqueue.insert(5)
        self.randomqueue.insert(2)
        self.randomqueue.insert(6)

        self.assertEqual(self.randomqueue.item[0], 5)
        self.assertEqual(self.randomqueue.item[1], 2)
        self.assertEqual(self.randomqueue.item[2], 6)

        self.assertFalse(self.randomqueue.is_empty())

    def test_get(self):
        self.randomqueue.insert(1)
        self.randomqueue.insert(2)
        self.randomqueue.insert(3)
        self.randomqueue.insert(4)
        self.randomqueue.insert(5)
        self.randomqueue.insert(6)
        self.randomqueue.insert(7)

        print(self.randomqueue.remove())
        print(self.randomqueue.remove())
        print(self.randomqueue.remove())
        print(self.randomqueue.remove())
        print(self.randomqueue.remove())
        print(self.randomqueue.remove())
        print(self.randomqueue.remove())

        try:
            self.randomqueue.remove()
        except Exception as e:
            self.assertEqual(IndexError, e.__class__)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
