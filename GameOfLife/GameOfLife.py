import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
red = 255, 0, 0

screen = pygame.display.set_mode(size)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	screen.fill(black)

	for x in range(50):
		for j in range(50):
		    screen.set_at((x, j), red) 
	
	
	pygame.draw.rect(screen, red, (10,100,10,100), 0)
	pygame.display.flip()