class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        
        r = 0
        k = 1
        f = True
        R = [[] for i in range(numRows)]
        
        R[r].append(s[0])
        
        for i in range(1, len(s)):
            if k == numRows:
                k = 1
                f = not f
                
            if f:
                r += 1
            else:
                r -= 1
                
            R[r].append(s[i])
            k += 1
            
        res = ''
        
        for row in R:
            res += ''.join(row)
            
        return res
