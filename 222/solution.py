import math

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

		left_h = self.leftHeight(root)
		ret = int(math.pow(2, left_h-1))
		
		n_leaves, done = [0], [False]
		self.countLeaves(root, done, n_leaves, 1, left_h)
		ret += n_leaves[0]

		return ret-1


	def leftHeight(self, node):
		if not node:
			return 0
		return 1 + self.leftHeight(node.left)

	def countLeaves(self, node, done, n_leaves, depth, left_h):

		if node.left:
			self.countLeaves(node.left, done, n_leaves, depth+1, left_h)

		if done[0]:
			return

		if depth == left_h:
			n_leaves[0] += 1

		if not node.right and depth < left_h:
			done[0] = True
			return

		if node.right:
			self.countLeaves(node.right, done, n_leaves, depth+1, left_h)

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