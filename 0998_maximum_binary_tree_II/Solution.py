# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            parent = TreeNode(val)
            parent.left = root
            return parent

        node = root
        parent = root
        while node.right and val < node.val:
            parent = node
            node = node.right

        if node.val >= val:
            node.right = TreeNode(val)
        else:
            parent.right = TreeNode(val)
            parent.right.left = node

        return root
