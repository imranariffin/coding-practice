class Solution(object):
    def getStringRange(self, a, b):
        if a == b:
            return '{0}'.format(a)
            
        return '{0}->{1}'.format(min(a, b), max(a, b))
        
        
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
            
        n = len(nums)
        res = []
        
        p1 = 0
        p2 = 0
        exp = nums[p1]
        
        while p1 < n and p2 < n:
            if nums[p2] == exp:
                p2 += 1
                exp += 1
            else:
                res.append(self.getStringRange(nums[p1], nums[p2 - 1]))
                p1 = p2
                p2 = p1
                exp = nums[p1]
                
        res.append(self.getStringRange(nums[p1], nums[p2 - 1]))
        
        return res
