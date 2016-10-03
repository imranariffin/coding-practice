class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		m = len(matrix)
		if m == 0:
			return []
		n = len(matrix[0])	
		if m == 1 and n == 1:
			return matrix[0]
		cycle = 0
		ret = []

		while len(ret) < n*m:
			if cycle%2 == 0:
				# horizontal
				if cycle%4 == 0:
					# top panel
					ret.extend(self.get_top_panel(matrix, cycle))
				else:
					# bottom panel
					ret.extend(self.get_bottom_panel(matrix, cycle))
			else:
				# vertical
				if (cycle+3)%4 == 0:
					# right panel
					ret.extend(self.get_right_panel(matrix, cycle))
				else:
					# left panel
					ret.extend(self.get_left_panel(matrix, cycle))

			cycle += 1
		return ret

	def get_column(self, matrix, j):
		return [row[j] for row in matrix]

	def get_top_panel(self, matrix, cycle):
		return matrix[cycle/4][cycle/4:None if cycle/4==0 else -(cycle/4)]

	def get_bottom_panel(self, matrix, cycle):
		m = len(matrix)
		return matrix[m - cycle/4 - 1][cycle/4:-(cycle/4 + 1)][::-1]

	def get_right_panel(self, matrix, cycle):
		n = len(matrix[0])
		return self.get_column(matrix, n-cycle/4-1)[cycle/4+1:None if cycle/4==0 else -(cycle/4)]

	def get_left_panel(self, matrix, cycle):
		return self.get_column(matrix, cycle/4)[cycle/4+1:-(cycle/4 + 1)][::-1]

if __name__=="__main__":
	s = Solution()
	s.spiralOrder([[1,2,3], [4,5,6], [7,8,9]])