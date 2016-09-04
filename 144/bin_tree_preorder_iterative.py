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

class Solution(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		ret = []
		stack = Stack()
		visited = set()
		if root != None:
			stack.push(root)
			visited.add(root)

		while not stack.empty():
			curr = stack.pop()
			len(stack.ls), curr
			ret.append(curr)
			visited.add(curr)

			if curr.right != None:
				stack.push(curr.right)
			if curr.left != None and curr.left not in visited:
				stack.push(curr.left)


		return [x.val for x in ret]

if __name__=="__main__":

	s = Solution()

	t = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None)))

	print s.preorderTraversal(t)