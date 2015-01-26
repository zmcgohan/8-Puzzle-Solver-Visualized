class Moves:
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3

class Node:
	def __init__(self, state, parent=None, action=None):
		self.state = state
		self.parent = parent
		self.action = action
		self.cost = parent.cost + 1 if parent is not None else 0
	def __hash__(self):
		return hash(self.state)
