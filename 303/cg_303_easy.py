class NumArray(object):
    # Fast solution based on clever memoization technique.
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sArr = []

        for e in nums:
            self.sArr += [e]

        for i in range(1, len(self.sArr)):
            self.sArr[i] = self.sArr[i] + self.sArr[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sArr[j]

        return self.sArr[j] - self.sArr[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
