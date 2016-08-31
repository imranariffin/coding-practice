"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
"""
class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		ret = []
		for i in range(len(nums)):
			start = i+1
			end = len(nums)-1			

			while start < end:
				a = nums[i]
				b = nums[start]
				c = nums[end]

				# print [a,b,c]
				if a+b+c == 0:
					# print "== ", [a,b,c]
					ret.append([a,b,c])
					# print (start, end,),
					start += 1
					end -= 1
					# print "->", (start, end,)
				elif a+b+c > 0:
					end -= 1
				else:
					start += 1


		# remove duplicates
		ret = self.remove_duplicates(ret)

		# print ret
		return ret

	def remove_duplicates(self, ls_triplets):
		s = set()
		ret = []
		for triplet in ls_triplets:
			triplet.sort()
			if tuple(triplet) not in s:
				ret.append(triplet)
			s.add(tuple(triplet))

		return ret

if __name__=="__main__":
	s = Solution()
	s.threeSum([-2,0,1,1,2])