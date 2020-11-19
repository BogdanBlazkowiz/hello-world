import pygame
import sys
import random
import pygame.freetype
from pygame.locals import *
from SnakeConfig import *

pygame.init()
Clock = pygame.time.Clock()


class Player:
	def __init__(self, width, position, color, dead, length, highscore):
		self.width = width
		self.position = position
		self.color = color
		self.dead = dead
		self.length = length
		self.highscore = highscore

	def randomise_position(self):
		self.position = random.randint(
			5, 125) * self.width, random.randint(5, 61) * self.width

	def eat_apple(self):
		self.length += 2
		self.highscore += 2


def cleanup_crew(positions_passees, player, rect_player):
	for f in positions_passees:
		cleanup_player1 = Rect(f, (player.width, player.width))
		pygame.draw.rect(screen, (0, 0, 0), cleanup_player1)
	cleanup_player1_2 = Rect(
		rect_player[0], rect_player[1], player.width, player.width)
	pygame.draw.rect(screen, (0, 0, 0), cleanup_player1_2)
	rect_player.move_ip(10000, 10000)
	player.length = 0
	player.dead = True


def check_collision(posx, posy):
	all_positions = [positions_passes_player1, positions_passes_player2,
					 positions_passes_player3, positions_passes_player4]
	for f in all_positions:
		if (posx, posy) in f:
			return True
	return False


GAME_FONT = pygame.freetype.SysFont("Arial", 20)
WIDTH_PLAYER = 10
running = False
direction1 = (1, 0)
direction2 = (-1, 0)
direction3 = (0, -1)
direction4 = (0, 1)
positions_passes_player1 = [(300, 160), (310,160)]
positions_passes_player2 = [(980, 480), (970, 480)]
positions_passes_player3 = [(320, 500), (320, 490)]
positions_passes_player4 = [(960, 140), (960, 150)]
position = (320, 160)
position2 = (960, 480)
position3 = (320, 480)
position4 = (960, 160)
player1 = Player(WIDTH_PLAYER, position, (255, 0, 0), False, 3, 1)
player2 = Player(WIDTH_PLAYER, position2, (0, 0, 255), False, 3, 1)
player3 = Player(WIDTH_PLAYER, position3, (0, 255, 0), False, 3, 1)
player4 = Player(WIDTH_PLAYER, position4, (255, 0, 255), False, 3, 1)
apple1 = Player(WIDTH_PLAYER, (random.randint(5, 125) * WIDTH_PLAYER,
							   random.randint(5, 61) * WIDTH_PLAYER),
				(255, 0, 0), True, 1, 1)
apple2 = Player(WIDTH_PLAYER, (random.randint(5, 125) * WIDTH_PLAYER,
							   random.randint(5, 61) * WIDTH_PLAYER),
				(0, 0, 255), True, 1, 1)
apple3 = Player(WIDTH_PLAYER, (random.randint(5, 125) * WIDTH_PLAYER,
							   random.randint(5, 61) * WIDTH_PLAYER),
				(0, 255, 0), True, 1, 1)
apple4 = Player(WIDTH_PLAYER, (random.randint(5, 125) * WIDTH_PLAYER,
							   random.randint(5, 61) * WIDTH_PLAYER),
				(255, 0, 255), True, 1, 1)
clear = Rect(0, 0, 2000, 30)
screen = pygame.display.set_mode((1280, 640))
pygame.display.set_caption("SnakeGame")
rect_player1 = Rect(player1.position, (player1.width, player1.width))
rect_player2 = Rect(player2.position, (player2.width, player2.width))
rect_player3 = Rect(player3.position, (player3.width, player3.width))
rect_player4 = Rect(player4.position, (player4.width, player4.width))
rect_apple1 = Rect(apple1.position, (apple1.width, apple1.width))
rect_apple2 = Rect(apple2.position, (apple2.width, apple2.width))
rect_apple3 = Rect(apple3.position, (apple3.width, apple3.width))
rect_apple4 = Rect(apple4.position, (apple4.width, apple4.width))
while True:
	pygame.draw.rect(screen, (255, 255, 255), clear)
	text_surface1, rect = GAME_FONT.render(
		"Highscore: " + str(player1.highscore), player1.color)
	text_surface2, rect = GAME_FONT.render(
		"Highscore: " + str(player2.highscore), player2.color)
	text_surface3, rect = GAME_FONT.render(
		"Highscore: " + str(player3.highscore), player3.color)
	text_surface4, rect = GAME_FONT.render(
		"Highscore: " + str(player4.highscore), player4.color)
	screen.blit(text_surface1, (10, 10))
	screen.blit(text_surface2, (160, 10))
	screen.blit(text_surface3, (310, 10))
	screen.blit(text_surface4, (460, 10))
	pygame.draw.rect(screen, apple1.color, rect_apple1)
	pygame.draw.rect(screen, apple2.color, rect_apple2)
	pygame.draw.rect(screen, apple3.color, rect_apple3)
	pygame.draw.rect(screen, apple4.color, rect_apple4)

	positions_passes_player1.append((rect_player1[0], rect_player1[1]))
	while len(positions_passes_player1) > player1.length + 1:
		positions_passes_player1.remove(positions_passes_player1[0])
	player1_shadow = Rect(
		positions_passes_player1[-player1.length],
		(WIDTH_PLAYER, WIDTH_PLAYER))
	pygame.draw.rect(screen, (0, 0, 0), player1_shadow)
	rect_player1.move_ip(
		direction1[0] * WIDTH_PLAYER, direction1[1] * WIDTH_PLAYER)

	positions_passes_player2.append((rect_player2[0], rect_player2[1]))
	while len(positions_passes_player2) > player2.length + 1:
		positions_passes_player2.remove(positions_passes_player2[0])
	player2_shadow = Rect(
		positions_passes_player2[-player2.length],
		(WIDTH_PLAYER, WIDTH_PLAYER))
	pygame.draw.rect(screen, (0, 0, 0), player2_shadow)
	rect_player2.move_ip(
		direction2[0] * WIDTH_PLAYER, direction2[1] * WIDTH_PLAYER)

	positions_passes_player3.append((rect_player3[0], rect_player3[1]))
	while len(positions_passes_player3) > player3.length + 1:
		positions_passes_player3.remove(positions_passes_player3[0])
	player3_shadow = Rect(
		positions_passes_player3[-player3.length],
		(WIDTH_PLAYER, WIDTH_PLAYER))
	pygame.draw.rect(screen, (0, 0, 0), player3_shadow)
	rect_player3.move_ip(
		direction3[0] * WIDTH_PLAYER, direction3[1] * WIDTH_PLAYER)

	positions_passes_player4.append((rect_player4[0], rect_player4[1]))
	while len(positions_passes_player4) > player4.length + 1:
		positions_passes_player4.remove(positions_passes_player4[0])
	player4_shadow = Rect(
		positions_passes_player4[-player4.length],
		(WIDTH_PLAYER, WIDTH_PLAYER))
	pygame.draw.rect(screen, (0, 0, 0), player4_shadow)
	rect_player4.move_ip(
		direction4[0] * WIDTH_PLAYER, direction4[1] * WIDTH_PLAYER)

	if check_collision(rect_player1[0], rect_player1[1]) or\
			rect_player1[0] == 0 or rect_player1[0] == 1270 \
			or rect_player1[1] == 30 or rect_player1[1] == 630:
		cleanup_crew(positions_passes_player1, player1, rect_player1)
		direction1 = (0, 0)

	if check_collision(rect_player2[0], rect_player2[1]) or\
			rect_player2[0] == 0 or rect_player2[0] == 1270 \
			or rect_player2[1] == 30 or rect_player2[1] == 630:
		cleanup_crew(positions_passes_player2, player2, rect_player2)
		direction2 = (0, 0)
	if check_collision(rect_player3[0], rect_player3[1]) or\
			rect_player3[0] == 0 or rect_player3[0] == 1270 \
			or rect_player3[1] == 30 or rect_player3[1] == 630:
		cleanup_crew(positions_passes_player3, player3, rect_player3)
		direction3 = (0, 0)
	if check_collision(rect_player4[0], rect_player4[1]) or\
			rect_player4[0] == 0 or rect_player4[0] == 1270 \
			or rect_player4[1] == 30 or rect_player4[1] == 630:
		cleanup_crew(positions_passes_player4, player4, rect_player4)
		direction4 = (0, 0)

	if (rect_player1[0], rect_player1[1]) == (rect_apple1[0], rect_apple1[1]):
		player1.eat_apple()
		apple1.randomise_position()
		rect_apple1 = Rect(apple1.position, (apple1.width, apple1.width))
	if (rect_player2[0], rect_player2[1]) == (rect_apple2[0], rect_apple2[1]):
		player2.eat_apple()
		apple2.randomise_position()
		rect_apple2 = Rect(apple2.position, (apple2.width, apple2.width))
	if (rect_player3[0], rect_player3[1]) == (rect_apple3[0], rect_apple3[1]):
		player3.eat_apple()
		apple3.randomise_position()
		rect_apple3 = Rect(apple3.position, (apple3.width, apple3.width))
	if (rect_player4[0], rect_player4[1]) == (rect_apple4[0], rect_apple4[1]):
		player4.eat_apple()
		apple4.randomise_position()
		rect_apple4 = Rect(apple4.position, (apple4.width, apple4.width))
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_LEFT] and not player1.dead:
		direction1 = (-1, 0)
	if pressed[pygame.K_DOWN] and not player1.dead:
		direction1 = (0, 1)
	if pressed[pygame.K_UP] and not player1.dead:
		direction1 = (0, -1)
	if pressed[pygame.K_RIGHT] and not player1.dead:
		direction1 = (1, 0)
	if pressed[pygame.K_z] and not player2.dead:
		direction2 = (0, -1)
	if pressed[pygame.K_d] and not player2.dead:
		direction2 = (1, 0)
	if pressed[pygame.K_q] and not player2.dead:
		direction2 = (-1, 0)
	if pressed[pygame.K_s] and not player2.dead:
		direction2 = (0, 1)
	if pressed[pygame.K_f] and not player3.dead:
		direction3 = (-1, 0)
	if pressed[pygame.K_g] and not player3.dead:
		direction3 = (0, 1)
	if pressed[pygame.K_t] and not player3.dead:
		direction3 = (0, -1)
	if pressed[pygame.K_h] and not player3.dead:
		direction3 = (1, 0)
	if pressed[pygame.K_i] and not player4.dead:
		direction4 = (0, -1)
	if pressed[pygame.K_l] and not player4.dead:
		direction4 = (1, 0)
	if pressed[pygame.K_j] and not player4.dead:
		direction4 = (-1, 0)
	if pressed[pygame.K_k] and not player4.dead:
		direction4 = (0, 1)
	if pressed[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.draw.rect(screen, player1.color, rect_player1)
	pygame.draw.rect(screen, player2.color, rect_player2)
	pygame.draw.rect(screen, player3.color, rect_player3)
	pygame.draw.rect(screen, player4.color, rect_player4)
	pygame.display.update()
	Clock.tick(20)
