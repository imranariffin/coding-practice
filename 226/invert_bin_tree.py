# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# import sys
# sys.path.insert(0, '..')
# import tree

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
        	return

        # mirror invert children
        temp = root.left
        root.left = root.right
        root.right = temp

        # recurse
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# if __name__=="__main__":

# 	# ls = [1, -2, -4, -1, 3, 2, 4, 9, 7, 6, 8, 11, 10, 12]
# 	ls = [1]
# 	t = tree.TreeNode(5)

# 	for n in ls:
# 		tree.addNode(t, tree.TreeNode(n))

# 	print "======"
# 	t.traverse_inorder_pretty()
# 	print "=inverted="
# 	s = Solution()
# 	s.invertTree(t)
# 	t.traverse_inorder_pretty()