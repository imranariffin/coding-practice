import heapq
class Solution(object):
	"""
	O(n + k*log(n))
	"""
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		nums = [-x for x in nums]
		heapq.heapify(nums)

		# ret = None
		# for i in range(k):
		# 	ret = heapq.heappop(nums)
		ret = heapq.nsmallest(k, nums)

		return -ret.pop()


if __name__=="__main__":
	ls_random = [14,2,100,134,134,1,55,66, 9, 123, -1]
	ls_sorted = [-x for x in ls_random]
	ls_sorted = sorted(ls_sorted)
	print ls_random
	print ls_sorted

	s = Solution()
	print s.findKthLargest(ls_random, 3)

# import heapq
# class Solution(object):
# 	"""
# 	O(k + (n-k)*logk)
# 	"""
# 	def findKthLargest(self, nums, k):
# 		"""
# 		:type nums: List[int]
# 		:type k: int
# 		:rtype: int
# 		"""
# 		# make min heap
# 		h = nums[0:k]
# 		heapq.heapify(h)

# 		# ret = heapq.nsmallest(k, nums)
# 		for i in nums[k:]:
# 			i
# 			if i > h[0]:
# 				heapq.heappush(h, i)

# 		# print h
# 		# print h
# 		# print "h[0]: ", h[0]
# 		# print heapq.nlargest(k, h)
# 		return heapq.nlargest(k, h).pop()


# if __name__=="__main__":
# 	# ls_random = [14,2,100,135,134,1,55,66, 9, 123, -1]
# 	ls_random = [5,2,4,1,3,6,0]
# 	# ls_sorted = [-x for x in ls_random]
# 	ls_sorted = [x for x in ls_random]
# 	ls_sorted = sorted(ls_sorted)
# 	print ls_random
# 	print ls_sorted

# 	s = Solution()
# 	print s.findKthLargest(ls_random, 4)