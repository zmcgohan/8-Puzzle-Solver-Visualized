from int_board import IntBoard
import solvers

if __name__ == '__main__':
	board = IntBoard()
	uninformed_graph_search_solver = solvers.UninformedGraphSearchSolver(board)
	print uninformed_graph_search_solver.solve_board()
