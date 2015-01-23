from board import Board
import solvers

if __name__ == '__main__':
	board = Board()
	solver = solvers.UninformedGraphSearchSolver(board)
	solver.solve_board()
