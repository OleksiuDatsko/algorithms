from binary_tree import BinaryTree

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    current = tree
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
            is_node = current == node
            current = current.right
    return None


v10 = root = BinaryTree(10)
v15 = root.right = BinaryTree(15)
v20 = root.right.right = BinaryTree(20)
v12 = root.right.right.left = BinaryTree(12)
v5 = root.left = BinaryTree(5)
v3 = root.left.left = BinaryTree(3)
v7 = root.left.right = BinaryTree(7)

# v10 = root = BinaryTree(10)
# v15 = root.right = BinaryTree(15)
# v20 = root.right.right = BinaryTree(20)
# v12 = root.right.left = BinaryTree(12)
# v5 = root.left = BinaryTree(5)
# v3 = root.left.left = BinaryTree(3)
# v7 = root.left.right = BinaryTree(7)

root.inorder()
root.travel(post=True)
print("result: ", find_successor(root, v10))
