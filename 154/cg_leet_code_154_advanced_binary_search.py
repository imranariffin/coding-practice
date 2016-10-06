class Solution(object):
    def minBinary(self, nums, start, end):
        mid = (start + end) / 2
        
        if start == end:
            return nums[mid]
            
        # Let us handle duplicates. We just do binary search to both partitions and return the minimum
        # result that we get. We don't choose since we don't know in which partition the characteristic
        # 'cliff' is.
        if nums[mid] == nums[end]:
            return min(self.minBinary(nums, start, mid), self.minBinary(nums, mid + 1, end))
        elif nums[mid] < nums[end]:
            return self.minBinary(nums, start, mid)
        else:
            return self.minBinary(nums, mid + 1, end)
            
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.minBinary(nums, 0, len(nums) - 1)
