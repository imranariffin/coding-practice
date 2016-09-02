class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def __str__(self):
		return "N({})".format(self.val)

	def traverse_inorder(self):
		if self == None:
			return

		traverse_inorder(self.left)
		print self.val
		traverse_inorder(self.right)

def addNode(root, treenode):

	if root == None:
		root = treenode
		return

	if treenode.val <= root.val:
		addNode(root.left, treenode)
	else:
		addNode(root.right, treenode)