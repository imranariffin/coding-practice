class Solution(object):
    def getPrint(self, a, b):
        if a == b:
            return '{0}'.format(a)
            
        return '{0}->{1}'.format(min(a, b), max(a, b))
        
        
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        curr = lower
        result = []
        
        for i in range(0, len(nums)):
            num = nums[i]
            
            if i != 0 and num == nums[i - 1]:
                continue
                
            if num == curr:
                curr += 1
            else:
                result.append(self.getPrint(curr, num - 1))
                curr = num + 1
                
        if curr <= upper:
            result.append(self.getPrint(curr, upper))
            
        return result
