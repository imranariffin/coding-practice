class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()

        for n in nums:
        	if n not in s:
        		s.add(n)
        	else:
        		s.remove(n)

        assert(len(s)==1)
        return s.pop()
