"""
use Counter
88 ms
"""

from collections import Counter

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		return [pair[0] for pair in Counter(nums).most_common(k)]

if __name__ == '__main__':
	s = Solution()
	print s.topKFrequent([1, 1, 1, 1, 2, 3, 4, 5, 6, 6, 6], 3)