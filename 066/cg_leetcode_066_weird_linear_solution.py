class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        c9 = 0
        
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                break
                
            c9 += 1
            
        if c9 >= n:
            return [1] + [0 for i in range(0, c9)]
            
        for i in range(0, c9):
            digits[n - 1 - i] = 0
            
        digits[n - 1 - c9] += 1
        
        return digits
