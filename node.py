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
	def __str__(self):
		nodes = [self]
		cur_node = self
		while cur_node.parent is not None:
			cur_node = cur_node.parent
			nodes.insert(0, cur_node)
		return_str = "{}".format(hash(nodes[0].state))
		for node in nodes[1:]:
			return_str += " -> {} ({})".format(hash(node.state), node.action)
		return return_str
