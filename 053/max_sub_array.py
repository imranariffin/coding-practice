"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		curr_sum = 0
		max_sum = nums[0]
		curr_sum = max_sum

		for i in range(1, len(nums)):
			n = nums[i]
			curr_sum = max(n, curr_sum+n)
			max_sum = max(max_sum, curr_sum)
		return max_sum