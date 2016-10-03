class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter1 = dict()
        counter2 = dict()

        for c in s:
            if c not in counter1:
                counter1[c] = 1
            else:
                counter1[c] += 1

        for c in t:
            if c not in counter2:
                counter2[c] = 1
            else:
                counter2[c] += 1
                
        for c in counter2:
            if c not in counter1:
                return c
            if counter2[c] != counter1[c]:
                return c

        assert(False)