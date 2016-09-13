class Solution(object):
	def countComponents(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: int
		"""
		ret = 0
		visited = set()
		g = self.clone_undigraph(n, edges)
		remaining = set([x for x in g])

		while n > 0:
			# pick a random node, traverse
			# collect into visited set
			node = remaining.pop()

			# traverse
			self.dfs(node, g, visited, remaining)

			n = len(remaining)
			ret += 1
		
		return ret

	def dfs(self, node, g, visited, remaining):
		if node in visited:
			return
		visited.add(node)
		remaining.discard(node)

		for v in g[node]:
			self.dfs(v, g, visited, remaining)

	def clone_undigraph(self, n, edges):
		g = {x: [] for x in range(0, n)}
		for e in edges:
			n1 = e[0]
			n2 = e[1]
			g[n1].append(n2)
			g[n2].append(n1)
		return g

if __name__=="__main__":
	s = Solution()
	edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [6, 7], [6, 8], [9, 10]]
	n = 11
	print s.countComponents(n, edges)