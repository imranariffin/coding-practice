class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        sumrows = [(r, sum(row)) for r, row in enumerate(mat)]
        toprows = sorted(sumrows, key=lambda x: (x[1], x[0]))[:k]

        return [r for r, _ in toprows]
