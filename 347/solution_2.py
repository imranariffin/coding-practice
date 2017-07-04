"""
sort-then-slice
72 ms
"""

from collections import Counter

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		frequencies = Counter(nums).items()
		# print frequencies
		return [e[0] for e in sorted(frequencies, key=lambda e: e[1], reverse=True)[:k]]

if __name__ == '__main__':
	s = Solution()
	print s.topKFrequent([1, 1, 1, 1, 2, 3, 4, 5, 6, 6, 6], 3)