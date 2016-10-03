class TreeNode(object):
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        use binary tree to reduce memory usage
        """

    def make_tree(self, x, n):
    	if n == 0:
    		return TreeNode(1)
    	if n == 1:
    		return TreeNode(x)

    	root = TreeNode(x)
    	node_stack = [root]
    	n_stack = [n]
    	
    	while node_stack:
    		# n = n_stack.pop()
    		# root = node_stack.pop()
    		n_left = n/2

    		while n_left > 0:
    			left = TreeNode(x)
    			root.left = left
    			node_stack.append(left)
    			n_stack.append(n_left)
    			root = root.left
    			n_left = n_left/2

    		root = node_stack.pop()
    		n = n_stack.pop()
    		print (root, n)
    		n_right = n-n/2

    		n = n-1