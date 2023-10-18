class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.value)

    def inorder(self) -> None:
        current = self
        stack = []
        result = []
        while stack or current:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(str(current))
                current = current.right
        print(" -> ".join(result))

    def travel(self, post: bool = False):
        if not self:
            return

        stack = [self]
        result = []
        while stack:
            current = stack.pop()
            result.append(str(current))
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        if post:
            result.reverse()
            print(" -> ".join(result))
        else:
            print(" -> ".join(result))