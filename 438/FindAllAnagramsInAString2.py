import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        chars = {c: 0 for c in string.lowercase}
        for c in p:
            chars[c] += 1
        ret = []
        if not s or len(p) > len(s):
            return ret
        start, end, count = 0, 0, len(p)
        while end < len(s):
            if end - start == len(p):
                if chars[s[start]] >= 0:
                    count += 1
                chars[s[start]] += 1
                start += 1
            chars[s[end]] -= 1
            if chars[s[end]] >= 0:
                count -= 1
            end += 1
            if count == 0:
                ret.append(start)
        return ret
