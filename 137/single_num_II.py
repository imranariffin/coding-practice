class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = dict()
        
        for n in nums:
            if n not in counter:
                counter[n] = 1
            elif counter[n] == 2:
                counter.pop(n)
            else:
                counter[n] += 1

        assert(len(counter)==1)
        return counter.popitem()[0]