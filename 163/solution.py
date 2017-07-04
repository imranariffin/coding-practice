class Solution(object):
	def findMissingRanges(self, nums, lower, upper):
		"""
		:type nums: List[int]
		:type lower: int
		:type upper: int
		:rtype: List[str]
		"""
		ret = []
		prev = lower - 1
		nums.append(upper+1)

		for n in nums:
			if n == prev+2:
				ret.append(str(n-1))
			elif n > prev+2:
				ret.append(str(prev+1) + "->" + str(n-1))

			prev = n

		return ret
		
if __name__ == '__main__':
	s = Solution()
	nums_0 = [0, 1, 3, 50, 75]
	lower = 0
	upper = 99
	print lower, upper, nums_0
	print s.findMissingRanges(nums_0, lower, upper)
	# assert(s.findMissingRanges(nums_0, lower, upper) == ["2", "4->49", "51->74", "76->99"])

	nums_1 = [0, 1, 3, 50, 75]
	lower = 0
	upper = 70
	print lower, upper, nums_1
	print s.findMissingRanges(nums_1, lower, upper)
	# assert(s.findMissingRanges(nums_1, lower, upper) == ["2", "4->49", "51->70"])

	nums_2 = [0, 1, 3, 50, 75]
	lower = 3
	upper = 70
	print lower, upper, nums_2
	print s.findMissingRanges(nums_2, lower, upper)

	nums_3 = [0, 1, 3, 48, 49, 50, 75, 80, 85]
	lower = 5
	upper = 99
	print lower, upper, nums_3
	print s.findMissingRanges(nums_3, lower, upper)

	nums_4 = [-1]
	lower = -2
	upper = -1
	print lower, upper, nums_4
	print s.findMissingRanges(nums_4, lower, upper)