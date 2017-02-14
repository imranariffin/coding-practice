class Solution(object):
	SIZE = 9
	def isValidSudoku(self, board):
		"""
		:type board: List[str]
		:rtype: bool
		"""
		for row in range(self.SIZE):
			for col in range(self.SIZE):
				if not self.is_valid(self.extract_row(board, row)):
					return False
				if not self.is_valid(self.extract_col(board, col)):
					return False
				if not self.is_valid(self.extract_box(board, row, col)):
					return False
		return True

	def is_valid(self, field):
		"""
		:type filed: str
		:rtype: boolean
		"""
		# is each number occurs no more than once
		counter = set()
		for n in field:
			if n != '.':
				if n not in counter:
					counter.add(n)
				else:
					return False
		return True

	def extract_col(self, board, col):
		"""
		:type board: List[str]
		:type col: int
		:rtype: List[str]
		"""
		return [board[row][col] for row in range(self.SIZE)]

	def extract_row(self, board, row):
		"""
		:type board: List[List[str]]
		:type row: int
		:rtype: List[str]
		"""
		return [e for e in board[row]]

	def extract_box(self, board, row, col):
		"""
		:type board: List[str]
		:type row: int
		:type col: int
		:rtype: List[str]
		"""
		b_row = row/3
		b_col = col/3
		
		istart = b_row*3
		iend = (b_row+1)*3
		jstart = b_col*3
		jend = (b_col+1)*3

		return [board[i][j] for i in range(istart, iend) for j in range(jstart, jend)]

def print_board(board):
	"""
	:type board: List[str]
	:rtype: None
	"""
	for row in board:
		print row

if __name__ == '__main__':
	s = Solution()

	print "=== TEST: init board_easy_0 ==="
	board_easy_0 = [
		'..5......',
		'2397546..',
		'8.....7.9',
		'.8...7.34',
		'4.6.3.9.5',
		'39.5...6.',
		'9.2.....7',
		'..3678592',
		'......1..'
	]
	print_board(board_easy_0)

	print "=== TEST: extract_col board_easy_0 ==="
	print "col=0:"
	print s.extract_col(board_easy_0, 0)
	print "col=1"
	print s.extract_col(board_easy_0, 1)
	print "col=8"
	print s.extract_col(board_easy_0, 8)

	print "=== TEST: extract_row board_easy_0 ==="
	print "row=0:"
	print s.extract_row(board_easy_0, 0)
	print "row=1"
	print s.extract_row(board_easy_0, 1)
	print "row=8"
	print s.extract_row(board_easy_0, 8)

	print "=== TEST: extract_box board_easy_0 ==="
	print "row=0,col=0:"
	print s.extract_box(board_easy_0, 0, 0)
	print "row=1,col=1"
	print s.extract_box(board_easy_0, 1, 1)
	print "row=2,col=2"
	print s.extract_box(board_easy_0, 2, 2)

	print "row=8,col=8"
	print s.extract_box(board_easy_0, 8, 8)
	print "row=6,col=6"
	print s.extract_box(board_easy_0, 6, 6)
	print "row=6,col=8"
	print s.extract_box(board_easy_0, 6, 8)
	print "row=8,col=6"
	print s.extract_box(board_easy_0, 8, 6)

	print "=== TEST: isValidSudoku board_easy_0 ==="
	print "board_easy_0:"
	print s.isValidSudoku(board_easy_0)

	print "=== TEST: init board_easy_1 ==="
	board_easy_1 = [
		".87654321",
		"2........",
		"3........",
		"4........",
		"5........",
		"6........",
		"7........",
		"8........",
		"9........"
	]
	print_board(board_easy_0)

	print "=== TEST: extract_col board_easy_1 ==="
	print "col=0:"
	print s.extract_col(board_easy_1, 0)
	print "col=1"
	print s.extract_col(board_easy_1, 1)
	print "col=8"
	print s.extract_col(board_easy_1, 8)

	print "=== TEST: extract_row board_easy_1 ==="
	print "row=0:"
	print s.extract_row(board_easy_1, 0)
	print "row=1"
	print s.extract_row(board_easy_1, 1)
	print "row=8"
	print s.extract_row(board_easy_1, 8)

	print "=== TEST: extract_box board_easy_1 ==="
	print "row=0,col=0:"
	print s.extract_box(board_easy_1, 0, 0)
	print "row=1,col=1"
	print s.extract_box(board_easy_1, 1, 1)
	print "row=2,col=2"
	print s.extract_box(board_easy_1, 2, 2)

	print "row=8,col=8"
	print s.extract_box(board_easy_1, 8, 8)
	print "row=6,col=6"
	print s.extract_box(board_easy_1, 6, 6)
	print "row=6,col=8"
	print s.extract_box(board_easy_1, 6, 8)
	print "row=8,col=6"
	print s.extract_box(board_easy_1, 8, 6)

	print "=== TEST: isValidSudoku board_easy_1 ==="
	print "board_easy_1:"
	print s.isValidSudoku(board_easy_1)