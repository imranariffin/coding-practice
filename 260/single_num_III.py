class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for n in nums:
        	xor ^= n

        r = xor&~(xor-1)

        res1 = 0
        res2 = 0
        for n in nums:
        	if r&n == 0:
        		res1 ^= n
        	else:
        		res2 ^= n

        return [res1, res2]


if __name__=="__main__":
	s = Solution()
	s.singleNumber([1,2,2,2,])