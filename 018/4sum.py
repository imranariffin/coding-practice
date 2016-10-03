class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ret = []
        nums.sort()

        # find 3sum for every i
        for i in range(len(nums)):
        	num = nums[i]
        	ret.extend(self.threeSumN(nums, target, ii, num))

	def threeSumN(self, nums, target, ii, N):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		# nums.sort()
		ret = []
		for i in range(len(nums)):
			if i != ii:
				start = i+1
				end = len(nums)-1

				while start < end:
					a = nums[i]
					b = nums[start]
					c = nums[end]

					# print [a,b,c]
					if -N+a+b+c == target:
						# print "== ", [a,b,c]
						ret.append([a,b,c])
						# print (start, end,),
						start += 1
						end -= 1
						# print "->", (start, end,)
					elif -N+a+b+c > target:
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