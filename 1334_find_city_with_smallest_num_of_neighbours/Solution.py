class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = [[float('inf')] * n for _ in range(n)]

        for u, v, w in edges:
            distances[u][v] = w
            distances[v][u] = w

        for u in range(n):
            distances[u][u] = 0

        for t in range(n):
            for v in range(n):
                for u in range(n):
                    distances[u][v] = min(
                        distances[u][v],
                        distances[u][t] + distances[t][v]
                    )

        ans = -1
        mincount = 1e99
        for u in range(n):
            count = 0
            for v in range(n):
                if u != v and distances[u][v] <= distanceThreshold:
                    count += 1
            if count <= mincount:
                mincount = count
                ans = u

        return ans

