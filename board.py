import random
from node import Moves

BOARD_WIDTH = 3

class Board:
	"""Represents a 3x3 board for an 8-puzzle."""
	def __init__(self, init_board=None):
		if init_board is not None:
			self.board = init_board
		else:
			digits = [i for i in xrange(BOARD_WIDTH**2)]
			random.shuffle(digits)
			self.board = []
			for i in xrange(BOARD_WIDTH**2):
				if i % BOARD_WIDTH == 0:
					self.board.append([])
				self.board[len(self.board)-1].append(digits[i])
	def get_adjacent_states(self):
		"""Returns a tuple containing all of the possible adjacent board hashes, as well as the moves to get there.
		
		Ex.: ((12345, ((3,2),2)), (39484, ((5,4),1)))"""
		# get position of blank tile
		print self
		adjacent_states = []
		blank_row, blank_col = 0, 0
		for row_num in xrange(len(self.board)):
			for col_num in xrange(len(self.board[row_num])):
				if self.board[row_num][col_num] == 0:
					blank_row = row_num
					blank_col = col_num
		print "Blank at row {}, col {}".format(blank_row, blank_col)
		if blank_row > 0:
			pass
		return [1, 2, 3]
	def __hash__(self):
		hash_code = 0
		for i in xrange(BOARD_WIDTH**2):
			hash_code *= 10
			hash_code += self.board[i / BOARD_WIDTH][i % BOARD_WIDTH]
		return hash_code
	def __str__(self):
		return_str = ''
		for row in self.board:
			for col in row:
				return_str += str(col) + ' '
			return_str += '\n'
		return return_str
	def get_goal_hash(self):
		return 12345678
