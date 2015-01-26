# TRIGGER WARNING: THIS CODE IS TERRIBLY FORMATTED
# I'm much more interested in the underlying logic of solving the puzzle in this case (ie. check out the other code) -- never plan on updating this visual code
import pygame as pg
from random import randint

INFO_CONTAINER_HEIGHT = 0
MOVE_VELOCITY = 100 # placeholder -- set in set_new_board

class BoardVisual:
	def __init__(self, surface):
		self.surface = surface
		self.clock = pg.time.Clock()
		self.moves = []
		self.move_distance = -1
	def set_new_board(self, board_int):
		"""Sets up internal representation of Pygame board spots."""
		global MOVE_VELOCITY
		self.moves = []
		self.board_spots = [[x for x in xrange(3)] for y in xrange(3)]
		spot_height = (self.surface.get_height()-INFO_CONTAINER_HEIGHT) / 3
		spot_width = self.surface.get_width() / 3
		MOVE_VELOCITY = spot_width * 7
		for i in xrange(9):
			cur_tile = (board_int % 10**(9-i)) / 10**(8-i)
			row, col = (i / 3, i % 3)
			if cur_tile == 9: 
				self.board_spots[row][col] = None
				continue
			# make tile surface and position on window
			self.board_spots[row][col] = []
			self.board_spots[row][col].append(pg.Surface((spot_width, spot_height)))
			self.board_spots[row][col][0].fill((0,0,0))
			self.board_spots[row][col].append([float(col*spot_width), float(row*spot_height)])
			# draw tile border
			inside_bg_rect = pg.Rect(3,3,spot_width-6,spot_height-6)
			pg.draw.rect(self.board_spots[row][col][0], (240,240,240), inside_bg_rect)
			# draw tile number
			tile_font = pg.font.Font(None, 80)
			tile_num_surface = tile_font.render(str(cur_tile), True, (0,0,0))
			tile_center_pos = (self.board_spots[row][col][0].get_width() / 2, self.board_spots[row][col][0].get_height() / 2)
			self.board_spots[row][col][0].blit(tile_num_surface, (tile_center_pos[0]-tile_num_surface.get_width()/2,tile_center_pos[1]-tile_num_surface.get_height()/2))
	def set_move_sequence(self, moves):
		self.moves = moves
	def get_empty_spot(self):
		"""Return the position of the empty spot in self.board_spots"""
		for row_num in xrange(len(self.board_spots)):
			for spot_num in xrange(len(self.board_spots[row_num])):
				if self.board_spots[row_num][spot_num] is None:
					return (row_num, spot_num)
	def move_up(self):
		empty_pos = self.get_empty_spot()
		moving_spot = self.board_spots[self.get_empty_spot()[0]-1][self.get_empty_spot()[1]]
		if self.move_distance == -1:
			self.move_distance = float(moving_spot[0].get_height())
		cur_dist = self.time_since_last_frame / 1000.0 * MOVE_VELOCITY
		moving_spot[1][1] += cur_dist
		self.move_distance -= cur_dist
		if self.move_distance < 0:
			moving_spot[1][1] -= -self.move_distance
			self.move_distance = -1
			self.board_spots[empty_pos[0]-1][empty_pos[1]] = None
			self.board_spots[empty_pos[0]][empty_pos[1]] = moving_spot
			#self.board_spots[self.get_empty_spot()[0]-1][self.get_empty_spot()[1]] = None
			#self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]] = moving_spot
			return True
		return None
	def move_right(self):
		empty_pos = self.get_empty_spot()
		moving_spot = self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]+1]
		if self.move_distance == -1:
			self.move_distance = float(moving_spot[0].get_width())
		cur_dist = self.time_since_last_frame / 1000.0 * MOVE_VELOCITY
		moving_spot[1][0] -= cur_dist
		self.move_distance -= cur_dist
		if self.move_distance < 0:
			moving_spot[1][0] += -self.move_distance
			self.move_distance = -1
			self.board_spots[empty_pos[0]][empty_pos[1]+1] = None
			self.board_spots[empty_pos[0]][empty_pos[1]] = moving_spot
			#self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]+1] = None
			#self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]] = moving_spot
			return True
		return None
	def move_down(self):
		empty_pos = self.get_empty_spot()
		moving_spot = self.board_spots[self.get_empty_spot()[0]+1][self.get_empty_spot()[1]]
		if self.move_distance == -1:
			self.move_distance = float(moving_spot[0].get_height())
		cur_dist = self.time_since_last_frame / 1000.0 * MOVE_VELOCITY
		moving_spot[1][1] -= cur_dist
		self.move_distance -= cur_dist
		if self.move_distance < 0:
			moving_spot[1][1] += -self.move_distance
			self.move_distance = -1
			self.board_spots[empty_pos[0]+1][empty_pos[1]] = None
			self.board_spots[empty_pos[0]][empty_pos[1]] = moving_spot
			#self.board_spots[self.get_empty_spot()[0]+1][self.get_empty_spot()[1]] = None
			#self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]] = moving_spot
			return True
		return None
	def move_left(self):
		empty_pos = self.get_empty_spot()
		moving_spot = self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]-1]
		if self.move_distance == -1:
			self.move_distance = float(moving_spot[0].get_width())
		cur_dist = self.time_since_last_frame / 1000.0 * MOVE_VELOCITY
		moving_spot[1][0] += cur_dist
		self.move_distance -= cur_dist
		if self.move_distance < 0:
			moving_spot[1][0] -= -self.move_distance
			self.move_distance = -1
			self.board_spots[empty_pos[0]][empty_pos[1]-1] = None
			self.board_spots[empty_pos[0]][empty_pos[1]] = moving_spot
			#self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]-1] = None
			#self.board_spots[self.get_empty_spot()[0]][self.get_empty_spot()[1]] = moving_spot
			return True
		return None
	def update(self):
		self.time_since_last_frame = self.clock.tick()

		if len(self.moves) > 0:
			if self.move_distance == -1:
				self.time_since_last_frame = 0
			cur_move = self.moves[0]
			cur_status = None
			if cur_move == 0: cur_status = self.move_up()
			elif cur_move == 1: cur_status = self.move_right()
			elif cur_move == 2: cur_status = self.move_down()
			elif cur_move == 3: cur_status = self.move_left()
			if cur_status:
				self.moves = self.moves[1:]
		# board
		board_surface = pg.Surface((self.surface.get_width(), self.surface.get_height() - INFO_CONTAINER_HEIGHT))
		board_surface.fill((240,240,240))
		for row in self.board_spots:
			for spot in row:
				if spot is not None:
					board_surface.blit(spot[0], spot[1])
		self.surface.blit(board_surface, (0,0))

		# info container
		info_container_rect = pg.Rect(0,self.surface.get_height()-INFO_CONTAINER_HEIGHT, self.surface.get_width(), INFO_CONTAINER_HEIGHT)
		pg.draw.rect(self.surface, (0,0,255), info_container_rect)

		pg.display.flip()
