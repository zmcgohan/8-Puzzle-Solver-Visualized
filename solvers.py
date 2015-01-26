from collections import deque
from node import Node
from int_board import IntBoard

class UninformedGraphSearchSolver:
	def __init__(self, board):
		self.board = board
	def solve_board(self):
		goal_hash = self.board.get_goal_hash()
		start_node = Node(self.board)
		past_nodes = set()
		past_nodes.add(hash(start_node))
		frontier = deque([start_node])
		while len(frontier) > 0:
			if (len(past_nodes) + len(frontier)) % 1000 == 0:
				print "len(past_nodes) = {}; len(frontier) = {}".format(len(past_nodes), len(frontier))
			cur_node = frontier.popleft()
			if hash(cur_node) == goal_hash: return cur_node
			for adjacent_board in cur_node.state.get_adjacent_boards():
				if adjacent_board[0] not in past_nodes:
					new_node = Node(IntBoard(adjacent_board[0]), cur_node, adjacent_board[1])
					past_nodes.add(hash(new_node))
					frontier.append(new_node)
		return False
