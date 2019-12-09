class Node:
    def __init__(self, v: int = 0, l = None, r = None, n = None):
        self.val = v
        self.left = l
        self.right = r
        self.next = n

    def __str__(self):
        return (
                f'[{hex(id(self))}: '
                f'v={self.val}, '
                f'l={self.left.val if self.left else None}, '
                f'r={self.right.val if self.right else None}, '
                f'n={self.next.val if self.next else None}]'
        )


class Solution:
    def connect(self, root):
        self._connect(None, root)
        return root

    def _connect(self, parent, node):
        if node is None:
            return
        node.next = self._getNext(parent, node)
        self._connect(node, node.right)
        self._connect(node, node.left)

    def _getNext(self, parent, node):
        if parent is None:
            return None
        if node is None:
            return None

        nextNode = parent
        while nextNode.next is not None:
            if nextNode.right == node:
                nextNode = nextNode.next
                continue
            if nextNode.left != node and nextNode.left is not None:
                return nextNode.left
            if nextNode.right != node and nextNode.right is not None:
                return nextNode.right
            nextNode = nextNode.next
        if nextNode.right == node:
            return None
        if nextNode.left == node:
            return nextNode.right
        return nextNode.left or nextNode.right

