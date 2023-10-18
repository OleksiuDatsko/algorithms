import unittest
from src.binary_tree import find_successor, BinaryTree


class TestBinaryTreeSuccessor(unittest.TestCase):
    def setUp(self):
        self.v10 = self.root = BinaryTree(10)
        self.v15 = self.root.right = BinaryTree(15)
        self.v20 = self.root.right.right = BinaryTree(20)
        self.v12 = self.root.right.right.left = BinaryTree(12)
        self.v5 = self.root.left = BinaryTree(5)
        self.v3 = self.root.left.left = BinaryTree(3)
        self.v7 = self.root.left.right = BinaryTree(7)

    def test_find_successor_v7(self):
        result = find_successor(self.root, self.v7)
        self.assertEqual(result, self.v10)

    def test_find_successor_v3(self):
        result = find_successor(self.root, self.v3)
        self.assertEqual(result, self.v5)

    def test_find_successor_v5(self):
        result = find_successor(self.root, self.v5)
        self.assertEqual(result, self.v7)

    def test_find_successor_v12(self):
        result = find_successor(self.root, self.v12)
        self.assertEqual(result, self.v20)

    def test_find_successor_v15(self):
        result = find_successor(self.root, self.v15)
        self.assertEqual(result, self.v12)

    def test_find_successor_v10(self):
        result = find_successor(self.root, self.v10)
        self.assertEqual(result, self.v15)
    
    def test_find_successor_v20(self):
        result = find_successor(self.root, self.v20)
        self.assertIsNone(result)
    


if __name__ == "__main__":
    unittest.main()
