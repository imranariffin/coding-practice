'''
Brute Force + Memoize
Time: O(n)
Space: O(n)
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = dict()
        return self.climb(0, n)
        
    def climb(self, i, n):
        if i in self.d:
            return self.d[i]
        if i > n:
            return 0
        if i == n:
            return 1
        self.d[i] = self.climb(i + 1, n) + self.climb(i + 2, n)
        return self.d[i]
