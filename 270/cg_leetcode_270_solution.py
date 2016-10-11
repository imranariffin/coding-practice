# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        curr = root
        res = curr.val
        
        while curr != None:
            if abs(curr.val - target) < abs(res - target):
                res = curr.val
                
            if curr.val == target:
                break
                
            if curr.val < target:
                curr = curr.right
            else:
                curr = curr.left
                
        return res
