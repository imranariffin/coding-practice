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

class Solution2(object):
  def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = self.countingSort(nums, maxint=20001)
    ret = []
    for i in range(0, len(nums), 2):
      ret.append(min(nums[i], nums[i + 1]))
    return sum(ret)

  def countingSort(self, nums, maxint=20001):
    counter = [0]*maxint
    base = 10000
    ret = []

    for n in nums:
      counter[base + n] += 1

    print counter
    for i, f in enumerate(counter):
      for j in range(f):
        ret.append(i - base)

    print ret
    return ret


if __name__ == '__main__':
  s = Solution2()

  nums = [1,4,3,2]
  ans = s.arrayPairSum(nums)
  exp = 4
  print "nums: {}\n expected: {}\n ans: {}\n".format(nums, exp, ans)

  nums = [1,4,3,2,-10000,10000]
  ans = s.arrayPairSum(nums)
  exp = 4
  print "nums: {}\n expected: {}\n ans: {}\n".format(nums, exp, ans)