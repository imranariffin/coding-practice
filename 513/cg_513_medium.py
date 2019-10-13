# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = -1
        self.leftmost_value = -1
        self.travel(root, 0)
        return self.leftmost_value

    def travel(self, node, d):
        if node == None:
            return
        if node.left == None and d > self.max_depth:
            self.max_depth = d
            self.leftmost_value = node.val
        self.travel(node.left, d + 1)
        self.travel(node.right, d + 1)
