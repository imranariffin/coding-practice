class Solution(object):
	def numberOfPatterns(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		grid = [[3*y+x+1 for x in range(3)] for y in range(3)]
		# for row in grid: print row
		self.number_of_patterns(grid, m, n)

	def number_of_patterns(self, grid, m, n):
		for i in range(2):
			for j in range(2):
				e = grid[i][j]
				# print e
				self.traverse(grid, i, j, [])


	def traverse(self, grid, i, j, visited):
		e = grid[i][j]
		visited.append(e)
		n = len(visited)
		print n, visited

		if n >= 5:
			return

		# vertical and horizontal moves
		if i+1 < 3 and grid[i+1][j] not in visited:
			self.traverse(grid, i+1, j, visited)
			visited.pop()
		if i-1 >= 0 and grid[i-1][j] not in visited:
			self.traverse(grid, i-1, j, visited)
			visited.pop()
		if j+1 < 3 and grid[i][j+1] not in visited:
			self.traverse(grid, i, j+1, visited)
			visited.pop()
		if j-1 >= 0 and grid[i][j-1] not in visited:
			self.traverse(grid, i, j-1, visited)
			visited.pop()

		# diagonal moves



if __name__=="__main__":
	s = Solution()
	s.numberOfPatterns(3, 3)