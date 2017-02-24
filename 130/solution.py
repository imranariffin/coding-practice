"""
exceeded recursion depth
"""

class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if not len(board): return
		maru_set = set()
		m = len(board)
		n = len(board[0])

		for i in range(m):
			for j in range(n):
				e = board[i][j]
				if (i, j) not in maru_set and e == "O":
					visited = set()
					if self.is_surrounded(visited, board, i, j):
						maru_set |= visited

		self.clear_maru(maru_set, board)

	def is_surrounded(self, visited, board, i, j):
		m = len(board)
		n = len(board[0])

		if i < 0 or i >= m or j < 0 or j >= n:
			return False
		if board[i][j] == 'X': 
			return True
		if (i, j) in visited: 
			return True
		
		visited.add((i, j))

		return (
			self.is_surrounded(visited, board, i-1, j) and
			self.is_surrounded(visited, board, i+1, j) and
			self.is_surrounded(visited, board, i, j-1) and
			self.is_surrounded(visited, board, i, j+1)
		)

	def clear_maru(self, visited, board):
		for i, j in visited:
			board[i][j] = 'X'

def print_board(board):
	for row in board:
		print row

if __name__ == '__main__':
	s = Solution()

	print "TEST is_surrounded"

	board_0 = [
		['X', 'X', 'X'],
		['X', 'O', 'X'],
		['X', 'X', 'X'],
	]
	visited = set()
	print "board_0: "
	print_board(board_0)
	print "is_surrounded(board_0, 1, 1)", s.is_surrounded(visited, board_0, 1, 1)
	assert(s.is_surrounded(set(), board_0, 1, 1) == True)
	s.clear_maru(visited, board_0)
	print "board_0 after: "
	print_board(board_0)
	
	board_1 = [
		['X', 'X', 'X'],
		['X', 'O', 'O'],
		['X', 'X', 'X'],
	]
	visited = set()
	print "board_1: "
	print_board(board_1)
	print "is_surrounded(board_1, 1, 1)", s.is_surrounded(visited, board_1, 1, 1)
	assert(s.is_surrounded(set(), board_1, 1, 1) == False)
	print "board_1 after: "
	print_board(board_1)

	board_1 = [
		['X', 'X', 'X'],
		['X', 'O', 'O'],
		['X', 'X', 'X'],
	]
	visited = set()
	print "board_1: "
	print_board(board_1)
	print "is_surrounded(board_1, 1, 2)", s.is_surrounded(visited, board_1, 1, 2)
	assert(s.is_surrounded(set(), board_1, 1, 2) == False)
	print "board_1 after: "
	print_board(board_1)

	board_2 = [
		['O', 'X', 'X'],
		['X', 'O', 'X'],
		['X', 'X', 'X'],
	]
	visited = set()
	print "board_2: "
	print_board(board_2)
	print "is_surrounded(board_2, 1, 1)", s.is_surrounded(visited, board_2, 1, 1)
	print "board_2 after: "
	s.clear_maru(visited, board_2)
	print_board(board_2)
	assert(s.is_surrounded(set(), board_2, 1, 1) == True)

	board_2 = [
		['O', 'X', 'X'],
		['X', 'O', 'X'],
		['X', 'X', 'X'],
	]
	print "board_2: "
	print_board(board_2)
	print "is_surrounded(board_2, 0, 0)", s.is_surrounded(set(), board_2, 0, 0)
	print "board_2 after: "
	print_board(board_2)
	assert(s.is_surrounded(set(), board_2, 0, 0) == False)

	board_3 = [
		['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X'],
		['X', 'X', 'O', 'X'],
		['X', 'X', 'X', 'X'],
	]
	visited = set()
	print "board_3: "
	print_board(board_3)
	print "is_surrounded(board_3, 1, 1)", s.is_surrounded(visited, board_3, 1, 1)
	assert(s.is_surrounded(set(), board_3, 1, 1) == True)
	s.clear_maru(visited, board_3)
	print "board_3 after: "
	print_board(board_3)

	board_3 = [
		['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X'],
		['X', 'X', 'O', 'X'],
		['X', 'X', 'X', 'X'],
	]
	visited = set()
	print "board_3: "
	print_board(board_3)
	print "is_surrounded(board_3, 1, 2)", s.is_surrounded(visited, board_3, 1, 2)
	assert(s.is_surrounded(set(), board_3, 1, 2) == True)
	s.clear_maru(visited, board_3)
	print "board_3 after: "
	print_board(board_3)

	board_3 = [
		['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X'],
		['X', 'X', 'O', 'X'],
		['X', 'X', 'X', 'X'],
	]
	visited = set()
	print "board_3: "
	print_board(board_3)
	print "is_surrounded(board_3, 2, 2)", s.is_surrounded(visited, board_3, 2, 2)
	assert(s.is_surrounded(set(), board_3, 2, 2) == True)
	s.clear_maru(visited, board_3)
	print "board_3 after: "
	print_board(board_3)

	board_3 = [
		['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'O'],
		['X', 'X', 'O', 'X'],
		['X', 'X', 'X', 'X'],
	]
	visited = set()
	print "board_3: "
	print_board(board_3)
	print "is_surrounded(board_3, 2, 2)", s.is_surrounded(visited, board_3, 2, 2)
	assert(s.is_surrounded(set(), board_3, 2, 2) == False)
	print "board_3 after: "
	print_board(board_3)

	print "TEST solve"

	board_4 = [
		['X', 'X', 'X', 'X', 'X'],
		['X', 'O', 'X', 'O', 'X'],
		['X', 'X', 'X', 'O', 'X'],
		['X', 'X', 'X', 'O', 'X'],
		['O', 'X', 'X', 'X', 'X'],
	]
	print "board_4:"
	print_board(board_4)
	s.solve(board_4)
	print "board_4 after:"
	print_board(board_4)

	board_5 = [
		['O', 'X', 'X', 'X', 'X'],
		['X', 'O', 'X', 'O', 'O'],
		['X', 'X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X', 'X'],
		['X', 'X', 'X', 'X', 'X'],
	]
	print "board_5:"
	print_board(board_5)
	s.solve(board_5)
	print "board_5 after:"
	print_board(board_5)

	board_6 = [
		['O', 'X', 'X', 'X', 'X'],
		['X', 'O', 'X', 'O', 'O'],
		['X', 'X', 'O', 'X', 'X'],
		['X', 'O', 'X', 'X', 'X'],
		['X', 'X', 'X', 'X', 'X'],
	]
	print "board_6:"
	print_board(board_6)
	s.solve(board_6)
	print "board_6 after:"
	print_board(board_6)

