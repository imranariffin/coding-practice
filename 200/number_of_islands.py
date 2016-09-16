class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		if len(grid) == 0:
			return 0

		grid = [[int(x) for x in row] for row in grid]
		nodes = self.get_nodes(grid)

		if len(nodes) == 0:
			return 0

		size = max(nodes)+1
		actual_size = size-len(nodes)
		edges = self.make_edges(grid, nodes)

		return self.countComponents(size, edges)-actual_size

	def get_nodes(self, grid):
		if len(grid) == 0:
			return []

		m = len(grid)
		n = len(grid[0])
		ret = [i*n+j if grid[i][j] == 1 else None for i in range(m) for j in range(n)]

		return filter(lambda x: x != None, ret)

	def make_edges(self, grid, nodes):
		if len(grid) == 0:
			return []

		edges = []
		m = len(grid)
		n = len(grid[0])

		visited = set()
		for node in nodes:
			x, y = node/n, node%n
			# print x, y

			if m > 1:
				if x > 0 and grid[x-1][y] == 1:
					e = [node, (x-1)*n+y]
					ee = ",".join(map(lambda x: str(x), [min(e), max(e)]))
					if ee not in visited:
						edges.append(e)
						visited.add(ee)

				if x < m-1 and grid[x+1][y] == 1:
					e = [node, (x+1)*n+y]
					ee = ",".join(map(lambda x: str(x), [min(e), max(e)]))
					if ee not in visited:
						edges.append(e)
						visited.add(ee)

			if n > 1:
				if y > 0 and grid[x][y-1] == 1:
					e = [node, x*n+y-1]
					ee = ",".join(map(lambda x: str(x), [min(e), max(e)]))
					if ee not in visited:
						edges.append(e)
						visited.add(ee)

				if y < n-1 and grid[x][y+1] == 1:
					e = [node, x*n+y+1]
					ee = [min(e), max(e)]
					ee = ",".join(map(lambda x: str(x), [min(e), max(e)]))
					if ee not in visited:
						edges.append(e)
						visited.add(ee)

		return edges

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
	# grid = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0]]
	# grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
	# grid = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
	# grid = [[1, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 1]]
	# grid = [[1, 0, 0, 0, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [1, 0, 0, 0, 1]]
	# grid = ["1","0","1","0","1","1"]
	# grid = [[1],[0],[1],[0],[1],[1]]
	grid = []
	grid = [[]]

	# grid = [[int(x) for x in row] for row in grid]
	# m = len(grid)
	# n = len(grid[0])

	# print "(m, n):", m, n
	# for row in grid: print row;

	# nodes = s.get_nodes(grid)
	# print "nodes:", nodes
	# size = max(nodes)+1
	# actual_size = size-len(nodes)
	# edges = s.make_edges(grid, nodes)
	# print "actual_size:", actual_size
	# print "size:", size
	# print nodes
	# print edges
	# print s.countComponents(size, edges)
	# print s.countComponents(size, edges)-actual_size
	print s.numIslands(grid)