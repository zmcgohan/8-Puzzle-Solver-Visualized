import random

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
	def __hash__(self):
		hash_code = 0
		for i in xrange(BOARD_WIDTH**2):
			hash_code *= 10
			hash_code += self.board[i / BOARD_WIDTH][i % BOARD_WIDTH]
		return hash_code
	def get_goal_hash(self):
		return 12345678
