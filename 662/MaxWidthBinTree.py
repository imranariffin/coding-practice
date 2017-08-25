# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d = dict()
        
    def traverse(self, t):
        self.__traverse__(t, 0, 0)
        
    def __traverse__(self, t, depth, i):
        if t == None:
            return
        
        if depth not in self.d:
            self.d[depth] = []
        
        self.d[depth].append(i)
        self.__traverse__(t.left, depth + 1, i * 2)
        self.__traverse__(t.right, depth + 1, i * 2 + 1)
        
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        
        ret = 0
        for depth in self.d:
            ret = max(ret, self.d[depth][-1] - self.d[depth][0] + 1)
            
        return ret
        
