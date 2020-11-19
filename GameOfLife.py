import pygame
from pygame.locals import *
import sys

size_block = 10
width = 720
height = 720
number_blocks_x = int(width/size_block)
number_blocks_y = int(height/size_block)

def closest_grid(position):
	posx = position[0]
	posy = position[1]
	grid = (int(posx/size_block)*size_block, int(posy/size_block)*size_block)
	return grid

def conways_game():
	new_grid = [[0 for x in range(number_blocks_x)] for x in range(number_blocks_y)] 
	def number_neighbours(index):
		lst = []
		number_of_living = 0
		number_of_dead = 0
		lst.append(grid_base[index[0]-1][index[1]])
		lst.append(grid_base[index[0]-1][index[1]+1])
		lst.append(grid_base[index[0]-1][index[1]-1])
		lst.append(grid_base[index[0]][index[1]+1])
		lst.append(grid_base[index[0]][index[1]-1])
		lst.append(grid_base[index[0]+1][index[1]-1])
		lst.append(grid_base[index[0]+1][index[1]])
		lst.append(grid_base[index[0]+1][index[1]+1])
		for f in lst:
			if f == 1:
				number_of_living += 1
			else:
				number_of_dead += 1
		return number_of_living, number_of_dead
	for f in range(len(grid_base)):
		for x in range(len(grid_base[0])):
			if f == 0 or f == len(grid_base)-1 or x == 0 or x == len(grid_base[1])-1:
				continue
			how_many_neighbours = number_neighbours((f,x))
			where_on_the_grid = grid_base[f][x]
			if where_on_the_grid == 1:
				if how_many_neighbours[0] == 2 or how_many_neighbours[0] == 3:
					new_grid[f][x] = 1
			elif where_on_the_grid == 0:
				if how_many_neighbours[0] == 3:
					new_grid[f][x] = 1
	return new_grid

def draw_stuff(grid):
	for f in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[f][x] == 1:
				(pygame.draw.rect(screen, (((x/number_blocks_x)*255), ((f/number_blocks_y)*(f/number_blocks_y)*255), ((f/number_blocks_y)*255)), [x*size_block, f*size_block, size_block, size_block]))

pygame.init()
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")
grid_base = [[0 for x in range(number_blocks_x)] for x in range(number_blocks_y)]
is_drawing = True
is_living = False

while is_drawing:
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	if pressed[pygame.K_SPACE]:
		is_drawing = False
		is_living = True
	mouse = pygame.mouse.get_pos()
	pressed = pygame.mouse.get_pressed()
	if pressed[0]:
		grid_pos = closest_grid(mouse)
		pygame.draw.rect(screen, (grid_pos[1]/width*255, grid_pos[0]/width*255, grid_pos[1]/width*255), [grid_pos[0], grid_pos[1], size_block, size_block])
		grid_base[(int(grid_pos[1]/size_block))][(int(grid_pos[0]/size_block))] = 1
	if pressed[2]:
		grid_pos = closest_grid(mouse)
		pygame.draw.rect(screen, (0, 0, 0), [grid_pos[0], grid_pos[1], size_block, size_block])
		grid_base[(int(grid_pos[1]/size_block))][(int(grid_pos[0]/size_block))] = 0
	Clock.tick(720)
	pygame.display.update()
while is_living:
	Clock.tick(12)
	grid_base = conways_game()
	screen.fill((0, 0, 0))
	draw_stuff(grid_base)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
