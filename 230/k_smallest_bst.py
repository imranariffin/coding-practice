"""
Given a binary search tree, write a function kthSmallest to find the kth 
smallest element in it.

Note: 
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to 
find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # traverse inorder with a counter

        ret = []
        self.__kth_smallest(root, k, ret)
        return ret[k-1]

    def __kth_smallest(self, root, k, ret):

    	# print "len(ret): ", len(ret), " k: ", k
    	# if len(ret) == k:
    	# 	return

    	if root == None:
    		return

    	self.__kth_smallest(root.left, k, ret)

    	if len(ret) >= k:
    		return

    	# print root.val    	

    	if len(ret) < k:
    		ret.append(root.val)

    	self.__kth_smallest(root.right, k, ret)

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

# if __name__=="__main__":
# 	ls = [-7, -5, -2, 2, 9, 1, 3, 7, 5, -6, 10]

# 	t = TreeNode(4)
# 	for n in ls:
# 		addNode(t, TreeNode(n))

# 	s = Solution()
# 	k = 3
# 	s.kthSmallest(t, k)
# 	print ls