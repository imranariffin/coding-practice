from collections import deque

class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		m = len(board)
		if not m: return
		n = len(board[0])

		# ls_margin = [(i, j) for i in [0, m-1] for j in range(n)]
		# ls_margin.extend([(i, j) for j in [0, n-1] for i in range(1, m-1)])
		ls_margin = []
		for i in range(m):
			for j in range(n):
				if (i in [0, m-1] or j in [0, n-1]) and board[i][j] == 'O':
					ls_margin.append((i, j))

		queue = deque(ls_margin)

		while queue:
			i, j = queue.popleft()

			# print i, j
			if i>=0 and i<m and j>=0 and j<n and board[i][j] == 'O':
				board[i][j] = 'M'

				if i-1>=0:
					queue.append((i-1, j))
				if i+1<m:
					queue.append((i+1, j))
				if j-1>=0:
					queue.append((i, j-1))
				if j+1<m:
					queue.append((i, j+1))

		for i in range(m):
			for j in range(n):

				if board[i][j] == 'M':
					board[i][j] = 'O'
				elif board[i][j] == 'O':
					board[i][j] = 'X'

def print_board(board):
	for row in board:
		print row

if __name__ == '__main__':
	s = Solution()

	print "TEST solve"

	board_3 = [
		"XOXX",
		"OXOX",
		"XOXO",
		"OXOX",
		"XOXO",
		"OXOX"
	]
	print "board_3:"
	print_board(board_3)
	s.solve(board_3)
	print "board_3 after:"
	print_board(board_3)

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
		['O', 'X', 'X', 'X', 'X', 'X'],
		['X', 'O', 'X', 'X', 'O', 'O'],
		['X', 'X', 'O', 'O', 'O', 'X'],
		['X', 'O', 'X', 'X', 'O', 'X'],
		['X', 'X', 'X', 'X', 'O', 'X'],
	]
	print "board_6:"
	print_board(board_6)
	s.solve(board_6)
	print "board_6 after:"
	print_board(board_6)

	board_7 = [
		"XXXXXXXXXXXXXXXXXXXX",
		"XXXXXXXXXOOOXXXXXXXX",
		"XXXXXOOOXOXOXXXXXXXX",
		"XXXXXOXOXOXOOOXXXXXX",
		"XXXXXOXOOOXXXXXXXXXX",
		"XXXXXOXXXXXXXXXXXXXX"
	]
	print "board_7:"
	print_board(board_7)
	s.solve(board_7)
	print "board_7 after:"
	print_board(board_7)

	expected = [
		"XXXXXXXXXXXXXXXXXXXX",
		"XXXXXXXXXOOOXXXXXXXX",
		"XXXXXOOOXOXOXXXXXXXX",
		"XXXXXOXOXOXOOOXXXXXX",
		"XXXXXOXOOOXXXXXXXXXX",
		"XXXXXOXXXXXXXXXXXXXX"
	]