import unittest


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leafs(top):
    if top is None:
        return
    if top.left is None and top.right is None:
        return 1
    return count_leafs(top.left) + count_leafs(top.right)


def count_total(top):
    if top is None:
        return 0
    else:
        if isinstance(top.data, (int, float)):
            return top.data + count_total(top.left) + count_total(top.right)
        else:
            raise ValueError("Węzły mszą mieć wartość liczbową!")


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)

    def test_count_leafs(self):
        self.assertEqual(count_leafs(self.root), 4)

    def test_count_total(self):
        self.assertEqual(count_total(self.root), 28)

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node("a")
        root.right.left = Node(6)
        root.right.right = Node(7)

        with self.assertRaises(ValueError):
            self.assertEqual(count_total(root), 23)

        self.root.left.left.left = Node(1.234)
        self.assertEqual(count_total(self.root), 29.234)


if __name__ == '__main__':
    unittest.main()
