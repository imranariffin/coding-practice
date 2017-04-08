"""
idea credit: /user/4dsys
"""
from math import pow

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

class Solution(object):
	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0

		left_h = self.getHeight(root.left)
		right_h = self.getHeight(root.right)

		if left_h == right_h:
			return int(pow(2, left_h)) + self.countNodes(root.right)
		else:
			return int(pow(2, right_h)) + self.countNodes(root.left)

	def getHeight(self, root):
		"""
		"""
		if not root:
			return 0
		return 1 + self.getHeight(root.left)

if __name__ == '__main__':
	sol = Solution()

	print "TEST0"
	root0 = TreeNode(5,
		TreeNode(3,
			TreeNode(2),
			TreeNode(4)),
		TreeNode(7,
			TreeNode(6),
			TreeNode(8)))
	print sol.countNodes(root0)

	print "TEST1"
	root1 = TreeNode(5,
		TreeNode(3,
			TreeNode(2),
			TreeNode(4)),
		TreeNode(7))
	print sol.countNodes(root1)

	print "TEST2"
	root2 = None
	print sol.countNodes(root2)

	print "TEST3"
	root3 = TreeNode(1)
	print sol.countNodes(root3)

	print "TEST4"
	root4 = TreeNode(2,
		TreeNode(1),
		TreeNode(3))
	print sol.countNodes(root4)

	print "TEST5"
	root5 = TreeNode(2, TreeNode(1), None)
	print sol.countNodes(root5)