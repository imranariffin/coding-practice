class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		mem = [[0 for x in range(n)] for y in range(m)]
		for i in range(m)[::-1]:
			for j in range(n)[::-1]:
				# pos = i*n+j
				# pos = (i, j)

				if i >= m-1 or j >= n-1:
					# mem[pos] = 1
					mem[i][j] = 1

				else:
					# pos_below = (pos[0]+1, pos[1])
					# pos_right = (pos[0], pos[1]+1)
					# pos_below = pos+n
					# pos_right = pos+1
					# mem[pos] = mem[pos_below] + mem[pos_right]
					mem[i][j] = mem[i+1][j] + mem[i][j+1]

				# curr_sum = 0
				# if i < m-1:
				# 	pos_below = (pos[0]+1, pos[1])
				# 	curr_sum = 1+mem[pos_below]
				# if j < n-1:
				# 	pos_right = (pos[0], pos[1]+1)
				# 	curr_sum = 1+mem[pos_right]
				# mem[pos] = curr_sum

		return mem[0][0]
		# return mem[(0, 0)]
		# return mem[0]