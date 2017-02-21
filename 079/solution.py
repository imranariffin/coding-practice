"""
DFS 472 ms
"""

class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if not len(board): return False
		if not len(word): return False

		m = len(board)
		n = len(board[0])
		searched = set()

		# self.print_board(board)
		for i in range(m):
			for j in range(n):
				depth = 0
				# print "dfs({}, {}, {})".format(i, j, word)
				if board[i][j] == word[0]:
					if self.dfs(searched, depth, board, i, j, word):
						return True
				# if self.dfs(searched, depth, board, i, j, word):
					# return True
		return False

	def print_board(self, board):
		for row in board:
			print row

	def dfs(self, searched, depth, board, i, j, word):
		length = len(word)
		m = len(board)
		n = len(board[0])

		if i < 0 or i >= m or j < 0 or j >= n:
			return False
		if depth >= length:
			return False
		if (i, j) in searched:
			return False

		searched.add((i, j))

		# print sorted(list(searched)), depth, length, i, j, "word[depth]:", word[depth], "board[i][j]:", board[i][j]
		# print word[depth],
		print " "*depth, board[i][j]

		if word[depth] != board[i][j]:
			searched.remove((i, j))
			return False

		# reached end of word
		if word[depth] == board[i][j] and depth >= length-1:
			return True

		# left
		if self.dfs(searched, depth+1, board, i, j-1, word):
			return True
		# top
		elif self.dfs(searched, depth+1, board, i-1, j, word):
			return True
		# right
		elif self.dfs(searched, depth+1, board, i, j+1, word):
			return True
		# bottom
		elif self.dfs(searched, depth+1, board, i+1, j, word):
			return True
		# not found
		else:
			searched.remove((i, j))
			return False

if __name__ == '__main__':
	s = Solution()

	print "TEST 0: 2x2 board"
	board_0 = [['A', 'B'], ['C', 'D']]
	assert(s.exist(board_0, 'BA'))
	assert(s.exist(board_0, 'CD'))
	assert(s.exist(board_0, 'AC'))
	assert(s.exist(board_0, 'CA'))
	assert(s.exist(board_0, 'BD'))
	assert(s.exist(board_0, 'DB'))
	assert(s.exist(board_0, 'A'))
	assert(s.exist(board_0, 'AB'))
	assert(s.exist(board_0, 'DC'))
	assert(s.exist(board_0, 'ABDC'))
	assert(s.exist(board_0, 'DCAB'))
	assert(s.exist(board_0, 'CABD'))
	assert(s.exist(board_0, 'CDBA'))
	assert(not s.exist(board_0, 'ABC'))
	assert(not s.exist(board_0, 'BC'))
	assert(not s.exist(board_0, 'CB'))
	assert(not s.exist(board_0, 'ABCD'))
	assert(not s.exist(board_0, 'ABCDB'))

	print "TEST 1: 4x4 board"
	board_1 = [	['A', 'B', 'C', 'D'], 
							['E', 'F', 'G', 'H'],
							['I', 'J', 'K', 'L'],
							['M', 'N', 'O', 'P']]
	assert(s.exist(board_1, 'ABCD'))
	assert(s.exist(board_1, 'DCBA'))
	assert(s.exist(board_1, 'AE'))
	assert(s.exist(board_1, 'AEIM'))
	assert(s.exist(board_1, 'MIEA'))
	assert(s.exist(board_1, 'ABFE'))
	assert(not s.exist(board_1, 'AEA'))
	assert(not s.exist(board_1, 'ABD'))
	assert(not s.exist(board_1, 'AF'))
	assert(not s.exist(board_1, 'KF'))
	assert(not s.exist(board_1, 'KLK'))
	assert(not s.exist(board_1, 'DAB'))
	assert(not s.exist(board_1, 'ABCF'))

	print "TEST 2 3:3 board"
	board_2 = ["CAA","AAA","BCD"]
	assert(s.exist(board_2, "AAB"))