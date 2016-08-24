class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            if nums[0] < nums[1]:   return nums[0]
            else:                   return nums[1]

        i = len(nums)/2
        mid = nums[i]
        rightmost = nums[len(nums)-1]

        # if middle is min
        if mid<nums[i-1] and mid<nums[i+1]:
            return mid

        # search in left or right sublist        
        if mid < rightmost:
            return self.findMin(nums[:i])
        else:
            return self.findMin(nums[i:])