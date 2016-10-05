# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # We don't need to keep track of visited nodes since we know that it's a tree.
    # Also, we don't need to visit nodes that are not reachable from the root.
    def dfs(self, node, ret):
        if node == None:
            return
        
        ret.append(node.val)
        
        for child in [node.left, node.right]:
            self.dfs(child, ret)
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        
        self.dfs(root, ret)
        
        return ret
        