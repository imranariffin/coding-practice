# Definition for a binary tree node.
class TreeNode(object):
	# def __init__(self, x):
	#     self.val = x
	#     self.left = None
	#     self.right = None
	def __init__(self, x, left, right):
	    self.val = x
	    self.left = left
	    self.right = right

	def __str__(self):
		return "N({})".format(self.val)

class Stack(object):
	def __init__(self):
		self.ls = []

	def push(self, x):
		self.ls.append(x)

	def pop(self):
		return self.ls.pop()

	def empty(self):
		return len(self.ls) == 0

	def peek(self):
		return self.ls[len(self.ls) - 1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if root == None:
			return []

		stack = Stack()
		visited = set()
		curr = root
		stack.push(curr)
		ret = []

		while True:
			
			# print [n.__str__() for n in stack.ls]

			while curr.left != None and curr not in visited:
				curr = curr.left
				stack.push(curr)
			# print [n.__str__() for n in stack.ls]

			curr = stack.pop()
			print curr
			visited.add(curr)
			ret.append(curr)

			if curr.right != None:
				curr = curr.right
				stack.push(curr)

			if stack.empty():
				break

		return [n.val for n in ret]

	def traverse_inorder(self, root, height):
		if root == None:
			return

		if root.right != None:
			self.traverse_inorder(root.right, height+1)
		print "--"*height, root.val
		if root.left != None:
			self.traverse_inorder(root.left, height+1)

if __name__=="__main__":

	s = Solution()

	t = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)))
	# t = TreeNode(2, TreeNode(3, TreeNode(1, None, None), None), None)

	print s.inorderTraversal(t)
	print s.traverse_inorder(t, 0)