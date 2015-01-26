"""Module for stuff related to an 8-puzzle board represented internally by an integer, which gets modified through only mathematical operations."""

from random import shuffle

class IntBoard:
	"""Board represented internally as an integer. 1-8 are the numbered tiles, 9 is empty."""
	def __init__(self, init_board=None):
		if init_board is not None:
			self.board_int = init_board
		else:
			shuffled_digits = [x for x in xrange(1,10)]
			shuffle(shuffled_digits)
			self.board_int = 0
			for digit in shuffled_digits:
				self.board_int *= 10
				self.board_int += digit
	def get_adjacent_boards(self):
		"""Returns a list of boards where the elements are tuples with the first element being the board's hash (also the internal repr in this case), and the second element being which direction the empty tile moved to make the new board.

		Ex.: [(912345678, 0), (912345678, 1)]"""
		adjacent_boards = []
		# get empty tile position
		empty_pos = -1
		for i in xrange(9):
			if (self.board_int % 10**(9-i)) / 10**(8-i) == 9:
				empty_pos = i
		# check if empty can be moved up (0)
		if empty_pos > 2:
			up_board = self.board_int
			switch_num = (up_board % 10**(9-empty_pos+3)) / 10**(8-empty_pos+3)
			up_board -= (9-switch_num)*10**(8-empty_pos)
			up_board += (9-switch_num)*10**(8-empty_pos+3)
			adjacent_boards.append((up_board, 0))
		# check if empty can be moved right (1)
		if empty_pos % 3 != 2:
			right_board = self.board_int
			switch_num = (right_board % 10**(9-empty_pos-1)) / 10**(8-empty_pos-1)
			right_board -= (9-switch_num)*10**(8-empty_pos)
			right_board += (9-switch_num)*10**(8-empty_pos-1)
			adjacent_boards.append((right_board, 1))
		# check if empty can be moved down (2)
		if empty_pos < 6:
			down_board = self.board_int
			switch_num = (down_board % 10**(9-empty_pos-3)) / 10**(8-empty_pos-3)
			down_board -= (9-switch_num)*10**(8-empty_pos)
			down_board += (9-switch_num)*10**(8-empty_pos-3)
			adjacent_boards.append((down_board, 2))
		# check if empty can be moved left (3)
		if empty_pos % 3 != 0:
			left_board = self.board_int
			switch_num = (left_board % 10**(9-empty_pos+1)) / 10**(8-empty_pos+1)
			left_board -= (9-switch_num)*10**(8-empty_pos)
			left_board += (9-switch_num)*10**(8-empty_pos+1)
			adjacent_boards.append((left_board, 3))
		return adjacent_boards
	def __hash__(self):
		return 912345678
	def __str__(self):
		temp_board_int = self.board_int
		board_str = ""
		for i in xrange(3):
			for j in xrange(3):
				divisor = 10**(8-(i*3+j))
				board_str += str(temp_board_int / divisor) + ' '
				temp_board_int %= divisor
			board_str += '\n'
		board_str = board_str.replace('9 ', '- ')
		return board_str

if __name__ == '__main__':
	int_board = IntBoard()
	print "Board:"
	print int_board
	print int_board.get_adjacent_boards()
