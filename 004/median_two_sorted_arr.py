class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		l = len(nums1)+len(nums2)
		

	def kth(self, a, b, k):
		if not a:
			return b[k]
		if not b:
			return a[k]

		ia, ib = len(a)/2, len(b)/2
		ma, mb = a[ia], b[ib]

		if ia+ib < k:
			if ma > mb:
				return self.kth(a, b[ib+1:],
					k-ib-1)
			else:
				return self.kth(a[ia+1:], b, 
					k-ia-1)
		else:
			if ma > mb:
				return self.kth(a[:ia], b, k)
			else:
				return self.kth(a, b[:ib], k)