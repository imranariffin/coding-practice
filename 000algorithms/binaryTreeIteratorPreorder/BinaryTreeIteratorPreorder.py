# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class BinaryTreeIteratorPreorder:
    def __init__(self, root):
        self.stack = []
        if not root:
            return

        self.stack.append(root)

    def hasnext(self):
        return len(self.stack) > 0
    
    def next(self):
        node = self.stack.pop()

        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)

        return node
