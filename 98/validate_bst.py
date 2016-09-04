# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, left, right):
		self.val = x
		self.left = left
		self.right = right

class Solution(object):
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root == None:
			return True

		print root.val, ": ", self.valid_node(root)

		return self.valid_node(root) and self.isValidBST(root.left) and self.isValidBST(root.right)

	def valid_node(self, node):

		if node == None:
			return True

		if node.left == None and node.right == None:
			return True

		elif node.left != None and node.right != None:
			return self.get_max(node.left) < node.val < self.get_min(node.right)

		elif node.left != None:
			return self.get_max(node.left) < node.val

		else:
			return node.val < self.get_min(node.right)

	def get_min(self, root):
		"""
		assumes root not null
		:type root: TreeNode
		:rtype: int
		"""
		if root.left != None:
			return self.get_min(root.left)
		return root.val

	def get_max(self, root):
		"""
		assumes root not null
		:type root: TreeNode
		:rtype: int
		"""
		if root.right != None:
			return self.get_max(root.right)
		return root.val

# if __name__=="__main__":

# 	# ls = [10,5,15,None,None,6,20, None, None, None, None]
# 	# for i in range()