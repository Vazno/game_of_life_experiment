from typing import Tuple
from dataclasses import dataclass
from copy import deepcopy
from time import sleep

from utils import replace_console_text, cls

@dataclass
class Cell():	
	alive: bool
	near: int = 0
	
	def __str__(self) -> str:
		if self.alive:
			return "*"
		else:
			return " "


class GameOfLife:
	def __init__(self, size: Tuple[int, int]) -> None:
		self.board = list()
		self.size = size

	def generate_board(self):
		self.board = list()
		for y in range(self.size[1]):
			self.board.append(list())
			for x in range(self.size[0]):
				self.board[-1].append(Cell(False, 0))

	def update_near_values(self):
		y = len(self.board)
		x = len(self.board[0])
		for row in range(y):
			for col in range(x):
				# clearing previous Cell.near vals
				self.board[row][col].near = 0
		def move(a, b, i, j):
			if i*j == 0:
				return (a+i)%x, (b+j)%y
			c_len = cycle_len(a, b, i , j)
			ctx = cycle_trans_x(a, b, i, j)
			cty = cycle_trans_y(a, b, i, j)
			return ctx + ((a+i-ctx)%c_len), cty + ((b+j-cty)%c_len)

		def cycle_trans_x(a, b, i, j):
			sign = 2*(i*j > 0) - 1
			return a - min(a, (y + sign*b - (sign<0))%y)

		def cycle_trans_y(a, b, i, j):
			sign = 2*(i*j > 0) - 1
			return b - min(b, (x + sign*a - (sign<0))%x)

		def cycle_len(a, b, i, j):
			if i*j > 0:
				return min(a, b) + min(x-a, y-b)
			else:
				return min(a, y-b-1) + min(x-a, b+1)

		offsets = [(-1, -1), (-1, 0), (-1, 1),
				(0, -1),           (0, 1),
				(1, -1), (1, 0), (1, 1)]

		checked = set()
		for row in range(y):
			for col in range(x):
				for offset in offsets:
					new_x, new_y = move(col, row, offset[1], offset[0])
					if col == 0 and row == 0 and (offset == (1, -1) or offset == (-1, 1)):
						pass
					elif col == self.size[0]-1 and row == self.size[1]-1 and (offset == (1, -1) or offset == (-1, 1)):
						pass
					elif col == 0 and row == self.size[1]-1 and (offset == (-1, -1) or offset == (1, 1)):
						pass
					elif col == self.size[0]-1 and row == 0 and (offset == (-1, -1) or offset == (1, 1)):
						pass
					else:
						if (row, col, new_y, new_x) in checked:
							pass
						else:
							checked.add((row, col, new_y, new_x))
							if self.board[new_y][new_x].alive:

								self.board[row][col].near += 1

	def next_move(self):
		for row in range(len(self.board)):
			for col in range(len(self.board[0])):
				if self.board[row][col].near == 3:
					self.board[row][col].alive = True
				elif self.board[row][col].near < 2:
					self.board[row][col].alive = False
				elif self.board[row][col].near > 3:
					self.board[row][col].alive = False
		self.update_near_values()

	def put_cell(self, pos: Tuple[int, int], alive=True):
		if pos[0] == self.size[0]:
			pos[0] -= 1
		if pos[1] == self.size[1]:
			pos[1] -= 1
		self.board[pos[1]][pos[0]] = Cell(alive)
		self.update_near_values()

	def print_board(self):
		text = "\n"
		new_matrix = deepcopy(self.board)
		for row in new_matrix:
			row.insert(0, "#")
			row.append("#")
		
		new_matrix.append(["#"]*(len(self.board[0])+2))
		new_matrix.insert(0, ["#"]*(len(self.board[0])+2))		
		for row in new_matrix:
			text += "".join([str(p) for p in row]) + "\n"

		self.text = text
		replace_console_text(text)

if __name__ == "__main__":
	from random import randint
	cls()
	game = GameOfLife([20, 10])
	game.generate_board()

	for i in range(40):
		game.put_cell([randint(0, len(game.board[0])), randint(0, len(game.board))])

	while True:
		game.print_board()
		sleep(0.5)
		game.next_move()