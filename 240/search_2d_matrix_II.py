# log (m+n)
class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		m = len(matrix)
		n = len(matrix[0])

		# start at left bottom and move one step
		# either up or right
		row = m-1
		col = 0
		while col < n and row >= 0:
			e = matrix[row][col]
			if e == target:
				return True
			elif m == 1 and n == 1:
				return False
			elif e < target:
				col += 1
			else:
				row -= 1
		return False

