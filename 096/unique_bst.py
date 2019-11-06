class Solution:

    def numTrees(self, n: int) -> int:
        cache = {0: 1, 1: 1}
        return self._numTrees(cache, n)

    def _numTrees(self, cache: dict, n: int) -> int:
        if n in cache:
            return cache[n]
        
        ret = 0
        for i in range(0, n):
            n_left = i
            n_right = n-i-1
            left = cache.get(
                n_left,
                self._numTrees(cache, n_left),
            )
            right = cache.get(
                n_right,
                self._numTrees(cache, n_right),
            )
            ret += left * right

        cache[n] = ret

        return ret
