import sys
import pygame

from Grid import Grid

pygame.init()

size = width, height = 800, 600
gridSize = (100, 100)
speed = [2, 2]
black = 0, 0, 0
red = 255, 0, 0

screen = pygame.display.set_mode(size)

grid = Grid(gridSize[0], gridSize[1], width, height, 5000)

print("Cell Size: ", grid.cellSize, "px")
print("Grid Size: ", grid.gridSize, "(rows, cols)")
clock = pygame.time.Clock()
time = 0
frame = 0
while 1:
	dt = clock.tick(60)
	time += dt

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	if time >= 1000:
		screen.fill(black)
		grid.printCells(screen, red, frame)
		grid.update()
		time = 0
		frame += 1



	pygame.display.flip()
