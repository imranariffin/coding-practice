class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sort in ascending
        nums.sort() # nlogn
        # majority element will always be in middle
        return nums[len(nums)/2]