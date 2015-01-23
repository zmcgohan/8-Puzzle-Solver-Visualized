from collections import deque

class UninformedGraphSearchSolver:
	def __init__(self, board):
		self.board = board
	def solve_board(self):
		goal_hash = self.board.get_goal_hash()
		past_boards = set()
		past_boards.add(self.board)
		frontier = deque([self.board])
		while len(frontier) > 0:
			cur_node = frontier.popleft()
			if hash(cur_node) == goal_hash: return 
		return 0
