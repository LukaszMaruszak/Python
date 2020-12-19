import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stos jest pełny!")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stos jest pusty!")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(3)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(5)
        self.assertEqual(self.stack.n, 1)
        self.assertEqual(self.stack.items[0], 5)

        self.stack.push(2)
        self.assertEqual(self.stack.n, 2)
        self.assertEqual(self.stack.items[0], 5)
        self.assertEqual(self.stack.items[1], 2)

        self.assertFalse(self.stack.is_empty())

        try:
            self.stack.push(10)
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

    def test_pop(self):
        self.stack.push(4)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 4)

        try:
            self.stack.pop()
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
