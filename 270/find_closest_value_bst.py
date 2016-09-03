# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
	def closestValue(self, root, target):
		"""
		:type root: TreeNode
		:type target: float
		:rtype: int
		"""
		if root == None:
			return None

		if root.left == None and root.right == None:
			return root.val

		if target < root.val:
			if root.left == None:
				return root.val

			max_left = self.get_max(root.left)
			if target > max_left:
				if self.abs_diff(max_left, target) < self.abs_diff(root.val, target):
					return self.closestValue(root.left, target)
				return root.val

			return self.closestValue(root.left, target)

		if target > root.val:
			if root.right == None:
				return root.val

			min_right = self.get_min(root.right)
			if target < min_right:
				if self.abs_diff(min_right, target) < self.abs_diff(root.val, target):
					return self.closestValue(root.right, target)
				return root.val

			return self.closestValue(root.right, target)

		else:
			return root.val

	def get_max(self, root):
		if root.right != None:
			return self.get_max(root.right)
		return root.val

	def get_min(self, root):
		if root.left != None:
			return self.get_min(root.left)
		return root.val

	def abs_diff(self, val1, val2):
		return abs(val1 - val2)

	def get_least_diff(self, target, ls_val):
		ls_diff = [abs(target - val) for val in ls_val]
		return ls_val[ls_diff.index(min(ls_diff))]