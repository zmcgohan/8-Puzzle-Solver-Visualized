from int_board import IntBoard
import solvers
import pygame as pg
from board_visual import BoardVisual
import sys

ENTER_KEY = 13

if __name__ == '__main__':
	pg.init()
	window = pg.display.set_mode((600,600))
	pg.display.set_caption("8-Puzzle Solver")
	set_new_board = True
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit(0)
			elif event.type == pg.KEYDOWN:
				if event.key == ENTER_KEY:
					set_new_board = True
		if set_new_board:
			set_new_board = False
			board = IntBoard()
			board_gui = BoardVisual(window)
			board_gui.set_new_board(hash(board))
			board_gui.update()
			uninformed_graph_search_solver = solvers.UninformedGraphSearchSolver(board)
			last_node = uninformed_graph_search_solver.solve_board()
			board_gui.set_move_sequence(last_node.get_move_sequence())
		board_gui.update()
