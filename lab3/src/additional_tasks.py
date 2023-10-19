from binary_tree import BinaryTree


def is_tree_balanced(node: BinaryTree) -> bool:
    def height(node: BinaryTree):
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        if abs(left - right) > 1:
            return False
        print(left, right, node)

        return max(left, right) + 1

    return bool(height(node))


def binary_tree_diameter(tree: BinaryTree) -> int:
    diameter = 0

    def height(node: BinaryTree):
        nonlocal diameter
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)

        if (
            node.left is not None
            and node.right is not None
            and (d := left + right) > diameter
        ):
            diameter = d

        return max(left, right) + 1

    height(tree)
    return diameter


# v10 = root = BinaryTree(10)
# v15 = root.right = BinaryTree(15)
# v20 = root.right.right = BinaryTree(20)
# v12 = root.right.right.left = BinaryTree(12)
# v5 = root.left = BinaryTree(5)
# v3 = root.left.left = BinaryTree(3)
# v7 = root.left.right = BinaryTree(7)

# v10 = root = BinaryTree(10)
# v15 = root.right = BinaryTree(15)
# v20 = root.right.right = BinaryTree(20)
# v12 = root.right.left = BinaryTree(12)
# v5 = root.left = BinaryTree(5)
# v3 = root.left.left = BinaryTree(3)
# v7 = root.left.right = BinaryTree(7)

v1 = root = BinaryTree(1)
v3 = root.left = BinaryTree(3)
v7 = root.left.left = BinaryTree(7)
v8 = root.left.left.left = BinaryTree(8)
v9 = root.left.left.left.left = BinaryTree(9)
v2 = root.right = BinaryTree(2)
v4 = v3.right = BinaryTree(4)
v5 = v4.right = BinaryTree(5)
v6 = v5.right = BinaryTree(6)

print("is balanced:", is_tree_balanced(root))
print("diameter:", binary_tree_diameter(root))
