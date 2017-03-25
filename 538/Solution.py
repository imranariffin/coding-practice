# Use max heap

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        max_heap = []
        self.makelist_traverse(root, max_heap)
        heapq.heapify(max_heap)
        
        prev_val = -heapq.heappop(max_heap)[0]
        sum_val = prev_val
        for i in range(len(max_heap)):
            t = heapq.heappop(max_heap)[1]
            
            cur_val = t.val
            if t.val < prev_val:
                t.val += sum_val
            sum_val += cur_val
            
        return root
        
    def makelist_traverse(self, tree, ls):
        if not tree:
            return
        
        ls.append((-tree.val, tree))
        
        if tree.left:
            self.makelist_traverse(tree.left, ls)
        if tree.right:
            self.makelist_traverse(tree.right, ls)
        return