class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        
        sList = list(map(str, s))
        vList = []
        
        for c in sList:
            if c in vowels:
                vList.append(c)
                
        for i in range(0, len(sList)):
            if sList[i] in vowels:
                sList[i] = vList.pop()
                
        return ''.join(sList)
