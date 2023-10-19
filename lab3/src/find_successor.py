from binary_tree import BinaryTree, inordef_reqursive


def find_successor(tree: BinaryTree, node: int) -> BinaryTree:
    current: BinaryTree = tree
    stack = []
    is_node = False

    while stack or current:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current, end=" -> ")
            if is_node:
                return current
            is_node = current.value == node
            current = current.right
    return None


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

root.inorder()
inordef_reqursive(root)
print()
print("result: ", find_successor(root, 2))
