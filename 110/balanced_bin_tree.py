# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#     def __str__(self):
#     	return "N({})".format(self.val)

#     def height(self):
#     	if self == None:
#     		return 0

#     	if self.left == None and self.right == None:
#     		return 1
#     	if self.left == None:
#     		return 1 + self.right.height()
#     	if self.right == None:
#     		return 1 + self.left.height()
#         return 1 + max([self.left.height(), self.right.height()])

class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		if root == None:
			return True

		if abs(self.height(root.left) - self.height(root.right)) > 1:
			return False

		return self.isBalanced(root.left) and self.isBalanced(root.right)

	def height(self, treenode):
		if treenode == None:
			return 0
		return 1 + max([self.height(treenode.left), self.height(treenode.right)])

# def addNode(root, treenode):
# 	if root == None:
# 		root = treenode
# 		return

# 	if treenode == None:
# 		return

# 	if treenode.val <= root.val:
# 		if root.left == None:
# 			root.left = treenode
# 		else:
# 			addNode(root.left, treenode)
# 	else:
# 		if root.right == None:
# 			root.right = treenode
# 		else:
# 			addNode(root.right, treenode)

# def traverse_inorder(root):
# 	if root == None:
# 		return

# 	print root.val
# 	traverse_inorder(root.left)
# 	traverse_inorder(root.right)

# def traverse_preorder_pretty(root):
# 	__traverse_preorder(root, 0)

# def __traverse_preorder(root, n):
# 	if root == None:
# 		return

# 	__traverse_preorder(root.right, n+1)
# 	print "  "*n, root.val	
# 	__traverse_preorder(root.left, n+1)

# if __name__=="__main__":

# 	t = TreeNode(3)

# 	for i in [1,2,2,3,None,None,3,4,None,None,4]:
# 		addNode(t, TreeNode(i))

# 	traverse_preorder_pretty(t)

# 	s = Solution()

# 	print s.height(t)

# 	lrc = t.left.right

# 	print s.height(lrc)
# 	lrlc = t.left.right.left
# 	lrrc = t.left.right.right
# 	print s.height(lrlc)
# 	print lrlc.height()
# 	print s.height(lrrc)
# 	print lrrc.height()
# 	print "lrc: ", s.isBalanced(lrc)

# 	lc = t.left
# 	print "lc: ", s.isBalanced(lc)

# 	print "t: ", s.isBalanced(t)

# 	T = None
# 	print s.isBalanced(T)