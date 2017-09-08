'''
Fibonacci solution
Time: O(n)
Space: O(1)
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        f, s = 1, 2
        for i in range(3, n + 1):
            t = f + s
            f = s
            s = t
        return s
