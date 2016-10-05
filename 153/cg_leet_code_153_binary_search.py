class Solution(object):
    def minBinary(self, nums, start, end):
        mid = (start + end) / 2
        
        if start == end:
            return nums[mid]
            
        if nums[mid] < nums[end]:
            return self.minBinary(nums, start, mid)
        else:
            return self.minBinary(nums, mid + 1, end)
            
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.minBinary(nums, 0, len(nums) - 1)
