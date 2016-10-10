class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        snums = sorted(nums)
        n = len(snums)
        i = 0
        res = []
        
        while i < n:
            if i != 0 and snums[i] == snums[i - 1]:
                i += 1
                continue
                
            p1 = i + 1
            p2 = n - 1
            target = -snums[i]
            
            while p1 < p2:
                sum2 = snums[p1] + snums[p2]
                
                if sum2 == target:
                    res.append([snums[i], snums[p1], snums[p2]])
                    p1 += 1
                    p2 -= 1
                    
                    while p1 < p2 and snums[p1] == snums[p1 - 1]:
                        p1 += 1
                        
                    while p1 < p2 and snums[p2] == snums[p2 + 1]:
                        p2 -= 1
                        
                elif sum2 < target:
                    p1 += 1
                    
                    while p1 < p2 and snums[p1] == snums[p1 - 1]:
                        p1 += 1
                        
                else:
                    p2 -= 1
                    
                    while p1 < p2 and snums[p2] == snums[p2 + 1]:
                        p2 -= 1
                        
            i += 1
            
        return res
