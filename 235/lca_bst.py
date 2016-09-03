# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # make p always > q    
        if p.val > q.val:
        	temp = TreeNode(p.val)
        	p = q
        	q = temp

        return self.__lowestCommonAncestor__(root, p, q)

    def __lowestCommonAncestor__(self, root, p, q):
       	if root == None:
       		return None

       	if p.val == root.val == q.val:
       		return root.val

       	if self.find(root, p) == None and self.find(root, q) == None:
       		return None

       	print root.val, p.val, q.val

       	if p.val < root.val and q.val > root.val:
       		if self.find(root.left, p) != None and self.find(root.right, q) != None:
       			return root.val
       		return None

       	if p.val < root.val and q.val < root.val:
       		return self.__lowestCommonAncestor__(root.left, p, q)

       	if p.val > root.val and q.val > root.val:
       		return self.__lowestCommonAncestor__(root.right, p, q)

       	if p.val == root.val:
       		if self.find(root.right, q) != None:
       			return root.val
       		return None

       	if q.val == root.val:
       		if self.find(root.left, p) != None:
       			return root.val
       		return None

    def find(self, root, node):
    	if root == None:
    		return None

    	if node.val < root.val:
    		return self.find(root.left, node)
    	if node.val > root.val:
    		return self.find(root.right, node)

    	return root

# def traverse_pretty(t, d):
# 	if t == None:
# 		return

# 	if t.right != None:
# 		traverse_pretty(t.right, d+1)
# 	print "--"*d, t.val
# 	if t.left != None:
# 		traverse_pretty(t.left, d+1)

# def addNode(root, treenode):
# 	if root == None:
# 		root = treenode
# 		return

# 	if treenode.val <= root.val:
# 		if root.left == None:
# 			root.left = treenode
# 			return
# 		addNode(root.left, treenode)
# 		return

# 	if root.right == None:
# 		root.right = treenode
# 		return
# 	addNode(root.right, treenode)

# if __name__=="__main__":

# 	# t = TreeNode(4)
# 	# t.left = TreeNode(2)
# 	# t.left.left = TreeNode(1)
# 	# t.left.right = TreeNode(3)
# 	# t.right = TreeNode(6)
# 	# t.right.left = TreeNode(5)
# 	# t.right.right = TreeNode(7)

# 	t = TreeNode(6)
# 	for i in [2,8,0,4,7,9, 3,5]:
# 		addNode(t, TreeNode(i))

# 	traverse_pretty(t, 1)

# 	s = Solution()

# 	print s.find(t, TreeNode(5))
# 	if s.find(t, TreeNode(10)):
# 		print "found 10"
# 	else:
# 		print "10 not found"

# 	# print s.lowestCommonAncestor(t, TreeNode(4), TreeNode(6))
# 	# print s.lowestCommonAncestor(t, TreeNode(2), TreeNode(6))
# 	# print s.lowestCommonAncestor(t, TreeNode(2), TreeNode(4))
# 	# print s.lowestCommonAncestor(t, TreeNode(5), TreeNode(7))
# 	# print s.lowestCommonAncestor(t, TreeNode(3), TreeNode(1))

# 	print s.lowestCommonAncestor(t, TreeNode(0), TreeNode(8))