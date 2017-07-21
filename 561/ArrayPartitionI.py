class Solution(object):
  def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    ret = []
    for i in range(0, len(nums), 2):
      ret.append(min(nums[i], nums[i + 1]))
    return sum(ret)
