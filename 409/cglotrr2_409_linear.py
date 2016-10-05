class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        charCountDict = dict()
        
        for c in s:
            if charCountDict.has_key(c):
                charCountDict[c] += 1
            else:
                charCountDict[c] = 1
                
        even = 0
        oddExist = False
        
        for key in charCountDict:
            val = charCountDict[key]
            
            if val % 2 == 0:
                even += val
            else:
                even += val - 1
                oddExist = True
                
        if oddExist:
            even += 1
        
        return even
