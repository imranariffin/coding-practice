class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = "aeiouAEIOU"
        # extract all vowels
        vowels = "".join([v for v in s if v in VOWELS])
        
        # reverse extracted vowels
        vowels = vowels[::-1]
        
        # replace vowels
        ret = []
        i = 0
        for c in s:
            if c in VOWELS:
                ret.append(vowels[i])
                i += 1
            else:
                ret.append(c)
        return "".join(ret)