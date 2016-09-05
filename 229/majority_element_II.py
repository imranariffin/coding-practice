class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		majors = set()
		count = dict()
		for num in nums:
			if num not in count.keys():
				count[num] = 1
			else:
				count[num] += 1

			if count[num] > len(nums)/3:
				if num not in majors:
					majors.add(num)

		return list(majors)