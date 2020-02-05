# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums = {}
        self.buildSums(root, sums)
        total = sums[root]
        cap = (10**9) + 7

        return self.cut(root, sums, total) % cap

    def cut(self, node, sums, total):
        if not node:
            return -1

        cutleft = (total - sums[node.left]) * sums[node.left] if node.left else -1
        cutright = (total - sums[node.right]) * sums[node.right] if node.right else -1
        nocutleft = self.cut(node.left, sums, total)
        nocutright = self.cut(node.right, sums, total)

        return max([cutleft, cutright, nocutleft, nocutright])

    def buildSums(self, node, sums):
        if not node:
            return

        self.buildSums(node.left, sums)
        self.buildSums(node.right, sums)

        sums[node] = node.val
        if node.left:
            sums[node] += sums[node.left]
        if node.right:
            sums[node] += sums[node.right]
