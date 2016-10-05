# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeStack = [root]
        preorder = []
        
        while len(nodeStack) > 0:
            node = nodeStack.pop()
            
            if node == None:
                continue
            
            preorder.append(node.val)
            
            # Put right child first to get correct sequence when we pop it later.
            for child in [node.right, node.left]:
                nodeStack.append(child)
        
        return preorder
        