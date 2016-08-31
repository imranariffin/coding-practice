class Solution(object):
    def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		next_board = [[cell for cell in row] for row in board]

		m = len(board)
		n = len(board[0])

		for i in range(m):
			for j in range(n):
				cell = board[i][j]
				neighbours = self.get_neighbours(board, i, j)
				n_live_neighbours = sum([1 for neighbour in neighbours.values() if neighbour==1])
				n_dead_neighbours = len(neighbours) - n_live_neighbours

				# if live cell
				if cell == 1:
					if n_live_neighbours < 2 or n_live_neighbours > 3:
						# die
						next_board[i][j] = 0
					if n_live_neighbours == 2 or n_live_neighbours == 3:
						# continue to live
						next_board[i][j] = 1
				# dead cell
				else:
					if n_live_neighbours == 3:
						# come back to life
						next_board[i][j] = 1

		# update board
		for i in range(m):
			for j in range(n):
				board[i][j] = next_board[i][j]

    def get_neighbours(self, board, i, j):
    	neighbours = {}
        m = len(board)
        n = len(board[0])

    	if j > 0:
    		neighbours['W'] = board[i][j-1]
    	if j < n-1:
    		neighbours['E'] = board[i][j+1]
    	if i > 0:
    		neighbours['N'] = board[i-1][j]
    	if i < m-1:
    		neighbours['S'] = board[i+1][j]

    	if i > 0 and j > 0:
    		neighbours['NW'] = board[i-1][j-1]
    	if i < m-1 and j < n-1:
    		neighbours['SE'] = board[i+1][j+1]
    	if i > 0 and j < n-1:
    		neighbours['NE'] = board[i-1][j+1]
    	if i < m-1 and j > 0:
    		neighbours['SW'] = board[i+1][j-1]

    	return neighbours

if __name__=="__main__":
	s = Solution()
	s.gameOfLife([[0,0,1,1], [0,1,1,0], [1,0,1,1], [0,0,0,1]])

