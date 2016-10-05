class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i in range(0, len(nums)):
            d[nums[i]] = i
            
        for i1 in range(0, len(nums)):
            num2 = target - nums[i1]
            
            if not d.has_key(num2):
                continue
            
            i2 = d[num2]
            
            if i2 != None and i2 != i1:
                return [i1, i2]
                
        return [-1, -1]
