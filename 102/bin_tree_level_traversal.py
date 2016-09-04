	# Definition for a binary tree node.
class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
	def __init__(self, x, left, right):
		self.val = x
		self.left = left
		self.right = right

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		h = self.height(root)
		ret = [[] for i in range(h)]

		self.__level_order__(root, 1, h, ret)
		return ret

	def __level_order__(self, root, depth, maxdepth, ret):
		if root == None:
			return

		if root.left == None and root.right == None:
			ret[depth-1].append(root.val)
			return

		if root.left != None and root.right != None:
			self.__level_order__(root.left, depth+1, maxdepth, ret)
			ret[depth-1].append(root.val)
			self.__level_order__(root.right, depth+1, maxdepth, ret)
			return

		if root.left == None:
			ret[depth-1].append(root.val)
			self.__level_order__(root.right, depth+1, maxdepth, ret)
			return

		if root.right == None:
			self.__level_order__(root.left, depth+1, maxdepth, ret)
			ret[depth-1].append(root.val)
			return

	def height(self, root):
		if root == None:
			return 0

		if root.left == None and root.right == None:
			return 1

		if root.left == None:
			return 1 + self.height(root.right)

		if root.right == None:
			return 1 + self.height(root.left)    	

		return 1 + max([self.height(root.left), self.height(root.right)])


if __name__=="__main__":

	# t = TreeNode(4, TreeNode(2, None, None), TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)))
	t = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(6, TreeNode(5, None, None), None))
	s = Solution()
	print s.height(t)
	print s.levelOrder(t)