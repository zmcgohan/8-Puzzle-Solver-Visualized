from int_board import IntBoard
import solvers
import pygame as pg
from board_visual import BoardVisual
import sys

if __name__ == '__main__':
	pg.init()
	window = pg.display.set_mode((600,600))
	pg.display.set_caption("8-Puzzle Solver")
	board_gui = BoardVisual(window)
	set_new_board = True
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit(0)
		if set_new_board:
			set_new_board = False
			board = IntBoard()
			board_gui.set_new_board(hash(board))
		board_gui.update()
	uninformed_graph_search_solver = solvers.UninformedGraphSearchSolver(board)
	print uninformed_graph_search_solver.solve_board()
