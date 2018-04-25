import numpy as np
import pygame
from random import randrange

class Grid(object):
	def __init__(self, rows, cols, screen_w, screen_h, cells_n=0):
		self.gridSize = self.rows, self.cols = rows, cols
		self.screen_w = screen_w
		self.screen_h = screen_h
		self.cellSize = self.cell_w, self.cell_h = round(screen_w / rows), round(screen_h / cols)
		self.grid = np.zeros(self.gridSize)
		self.t_grid = np.zeros(self.gridSize)
		self.fillGrid(cells_n)

	def printCells(self, screen, color, frame):
		for x in range(self.gridSize[0]):
			for y in range(self.gridSize[1]):
				if self.grid[x, y] == 1:
					pygame.draw.rect(screen, color, (x * self.cell_w, y * self.cell_h, self.cell_w, self.cell_h), 0)

	def fillGrid(self, n=0):
		for x in range(n):
			a = randrange(0, self.rows-1)
			b = randrange(0, self.cols - 1)
			self.grid[a, b] = 1
	def update(self):
		#Iterate the matrix
		for x in range(self.rows):
			for y in range(self.cols):
				#iterate cells around
				neighbour_cells = 0
				for i in range(-1, 2):
					for j in range(-1, 2):
						if x+1 < self.cols and x-1 >= 0 and y+1 < self.rows and y-1 >= 0:
							if i != 0 and j != 0:
								if self.grid[x+i, y+j] == 1:
									neighbour_cells += 1
				if neighbour_cells > 3 or neighbour_cells < 2:
					self.t_grid[x, y] = 0
				elif neighbour_cells == 3:
					self.t_grid[x, y] = 1
				else:
					self.t_grid[x, y] = self.grid[x, y]
		self.grid = self.t_grid