import unittest


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self): # O(N)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:   # self.length == 1
            node = self.tail
            self.head = self.tail = None
        else:
            i = self.head
            while i.next != self.tail:
                i = i.next
            self.tail = i
            self.tail.next = i.next
            node.next = None
            self.length -= 1
            return node     # zwracamy usuwany node

    def merge(self, other): # O(1)
        if not isinstance(other, SingleList):
            raise ValueError("Można połączyć tylko SingleList")
        if other.length == 0:
            raise ValueError("Chcesz dołączyć pustą listę")
        # self jest pust lista
        if self.length == 0:
            self.head = other.head
            self.tail = other.tail
        # self ma tylko jeden element
        if self.head == self.tail:
            self.head.next = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
        self.length += other.length
        other = None
        return self     # zwraca połączoną listę

    def clear(self):
        self.head = self.tail = None
        self.length = 0
        return self     # zwraca pustą listę


# Kod testujący moduł.


class TestSingleList(unittest.TestCase):

    def setUp(self):
        self.lista1234 = SingleList()
        self.lista1234.insert_head(Node(1))
        self.lista1234.insert_tail(Node(2))
        self.lista1234.insert_tail(Node(3))
        self.lista1234.insert_tail(Node(4))
        # lista1234 [1, 2, 3, 4]

        self.listaabcd = SingleList()
        self.listaabcd.insert_head(Node("a"))
        self.listaabcd.insert_tail(Node("b"))
        self.listaabcd.insert_tail(Node("c"))
        self.listaabcd.insert_tail(Node("d"))
        # listaabcd [a, b, c, d]

        self.listapusta = SingleList()

    def test_remove_tail(self):
        self.assertEqual(self.lista1234.remove_tail().data, 4)
        self.assertEqual(self.lista1234.remove_tail().data, 3)
        self.assertEqual(self.lista1234.remove_tail().data, 2)

        self.assertEqual(self.listaabcd.remove_tail().data, "d")
        self.assertEqual(self.listaabcd.remove_tail().data, "c")
        self.assertEqual(self.listaabcd.remove_tail().data, "b")

        with self.assertRaises(ValueError):
            self.listapusta.remove_tail()

    def test_merge(self):
        self.lista1234.merge(self.listaabcd)
        self.assertEqual(self.lista1234.length, 8)
        self.assertEqual(self.lista1234.head.data, 1)
        self.assertEqual(self.lista1234.tail.data, "d")
        self.assertEqual(self.lista1234.remove_tail().data, "d")
        self.assertEqual(self.lista1234.remove_tail().data, "c")
        self.assertEqual(self.lista1234.remove_tail().data, "b")
        self.assertEqual(self.lista1234.remove_tail().data, "a")
        self.assertEqual(self.lista1234.remove_tail().data, 4)
        self.assertEqual(self.lista1234.remove_tail().data, 3)
        self.assertEqual(self.lista1234.remove_tail().data, 2)
        self.assertEqual(self.lista1234.remove_head().data, 1)

        with self.assertRaises(ValueError):
            self.lista1234.merge("[1, 2, 3, 4]")

        with self.assertRaises(ValueError):
            self.lista1234.merge(self.listapusta)

    def test_clear(self):
        self.lista1234.clear()
        self.listaabcd.clear()
        self.assertEqual(self.lista1234.length, 0)
        self.assertEqual(self.listaabcd.length, 0)


if __name__ == '__main__':
    unittest.main()
