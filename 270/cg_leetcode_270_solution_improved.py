# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # See "https://discuss.leetcode.com/topic/37526/clean-python-code".
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = root.val
        
        while root != None:
            if abs(root.val - target) < abs(res - target):
                res = root.val
                
            root = root.left if target < root.val else root.right
            
        return res
