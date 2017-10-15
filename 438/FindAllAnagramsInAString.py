import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pd, sd = dict(), dict()
        pc, sc = collections.Counter(p), collections.Counter(s[:len(p)])
        compare = {k: pc[k] == sc[k] for k in set(pc.elements())}
        
        ret = []
        n = len(s) - len(p) + 1
        lenp = len(p)
        
        for i in range(n):
            # print sc, compare
            if len(compare) == sum(compare.values()):
                ret.append(i)
            if i != n - 1:
                sc[s[i]] -= 1
                sc[s[i + lenp]] += 1
                compare[s[i]] = sc[s[i]] == pc[s[i]]
                compare[s[i + lenp]] = sc[s[i + lenp]] == pc[s[i + lenp]]
                
        return ret
