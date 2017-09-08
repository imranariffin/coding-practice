class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = dict()
        self.nums = nums
        if not nums:
            return
        self.dp[0] = nums[0]
        for i in range(1, len(nums)):
            self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - self.dp[i] + self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
