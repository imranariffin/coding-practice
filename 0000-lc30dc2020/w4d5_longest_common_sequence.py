class SolutionDpTopDown:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def lcs(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            cur = 1 if text1[i] == text2[j] else 0
            if cur:
                ret = cur + lcs(i - 1, j - 1)
            else:
                ret = max(
                    lcs(i, j - 1),
                    lcs(i - 1, j),
                )
            memo[(i, j)] = ret
            return ret

        return lcs(len(text1) - 1, len(text2) - 1)


class SolutionDpTopDownLRU:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.lru_cache(maxsize=1000 * 1000)
        def lcs(i, j):
            if i < 0 or j < 0:
                return 0
            cur = 1 if text1[i] == text2[j] else 0
            if cur:
                ret = cur + lcs(i - 1, j - 1)
            else:
                ret = max(
                    lcs(i, j - 1),
                    lcs(i - 1, j),
                )
            return ret

        return lcs(len(text1) - 1, len(text2) - 1)


class SolutionDpBottomUp:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [
            [0 for _ in range(n + 1)]
            for _ in range(m + 1)
        ]

        for i, row in enumerate(memo):
            if i == 0:
                continue
            for j, cell in enumerate(row):
                if j == 0:
                    continue
                if text1[i - 1] == text2[j - 1]:
                    memo[i - 1][j - 1] = 1 + memo[i - 2][j - 2]
                else:
                    memo[i - 1][j - 1] = max(
                        memo[i - 1][j - 2],
                        memo[i - 2][j - 1],
                    )

        return memo[m - 1][n - 1]
