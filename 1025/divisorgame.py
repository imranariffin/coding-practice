from typing import List


class Solution:
    def divisorGame(self, n: int) -> bool:
        memo = [[0]*n, [0]*n]
        memo[0][0] = -1
        memo[1][0] = 1
        return self.helper(n, True, memo)

    def helper(
            self,
            n: int,
            isalice: bool,
            memo: List[List[int]]
    ) -> bool:
        if isalice and n == 1:
            return False
        if not isalice and n == 1:
            return True

        if memo[isalice][n-1]:
            return memo[isalice][n] == 1

        results = set()
        for i in range(1, n):
            if n%i == 0:
               results.add(self.helper(n-i, not isalice, memo))

        ret = (
            any(results) if isalice
            else all(results)
        )

        memo[isalice][n-1] = [-1, 1][ret]

        return ret

