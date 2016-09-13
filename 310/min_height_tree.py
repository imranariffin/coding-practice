class Solution(object):
	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		g = self.clone_graph(n, edges)
		ret = []

		while n > 2:
			ls_leaves = [x for x in g if len(g[x]) == 1]
			for leaf in ls_leaves:
				# cut off the edge between a leaf and one neighbor
				node = g[leaf].pop()
				if len(g[leaf]) == 0:
					g.pop(leaf)
				g[node].remove(leaf)

			n -= len(ls_leaves)

		return [x for x in g]

	def clone_graph(self, n, edges):
		g = {x: [] for x in range(0, n)}
		for e in edges:
			n1 = e[0]
			n2 = e[1]
			g[n1].append(n2)
			g[n2].append(n1)
		return g

if __name__=="__main__":
	s = Solution()
	# s.find_leaves(4, [[1, 0], [1, 2], [1, 3]])
	edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [5, 6], [4, 7], [7, 8], [8, 9], [9, 10], [10, 11]]
	n = 12
	g = s.clone_graph(n, edges)

	print edges
	print g
	ls_leaves = [x for x in g if len(g[x]) <= 1]
	print ls_leaves

	print s.findMinHeightTrees(n, edges)