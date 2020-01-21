# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None
        self.remove(root.left, target, root, True)
        self.remove(root.right, target, root, False)
        if self.is_leaf(root) and root.val == target:
            return None
        return root

    def remove(self, root, target, parent, is_left):
        if root is None:
            return None

        self.remove(root.left, target, root, True)
        self.remove(root.right, target, root, False)

        if self.is_leaf(root) and root.val == target:
            if is_left:
                parent.left = None
            else:
                parent.right = None

    def is_leaf(self, node):
        return node.left is None and node.right is None
