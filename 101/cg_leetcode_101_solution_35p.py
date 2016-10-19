# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        l = [root.left]
        r = [root.right]
        
        while l or r:
            lNode = l.pop()
            rNode = r.pop()
            
            lVal = None
            rVal = None
            
            if lNode:
                lVal = lNode.val
                
                for node in [lNode.left, lNode.right]:
                    l.append(node)
                    
            if rNode:
                rVal = rNode.val
                
                for node in [rNode.right, rNode.left]:
                    r.append(node)
                    
            if lVal != rVal:
                return False
            
        return True
