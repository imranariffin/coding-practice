# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def recurse(nums):
            if not nums:
                return None

            maxn = max(nums)
            maxi = nums.index(maxn)
            node = TreeNode(maxn)
            node.left = recurse(nums[:maxi])
            node.right = recurse(nums[maxi+1:])

            return node

        return recurse(nums)
