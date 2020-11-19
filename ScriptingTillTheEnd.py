import pygame
import pygame.freetype
from math import exp
import sys
from pygame.locals import *


class Boughtables():
	def __init__(self, ammount, total_bought, power, cost_exp_mult, produced, cost_base):
		self.ammount = ammount
		self.total_bought = total_bought
		self.power = power
		self.cost_exp_mult = cost_exp_mult
		self.produced = produced
		self.cost_base = cost_base

	def cost_buy(self, indice):
		total_sum = 0
		temp_temp = self.total_bought
		for f in range(indice):
			total_sum += self.cost_base * self.cost_exp_mult**self.total_bought
			self.total_bought += 1
		self.total_bought = temp_temp
		return total_sum


def big_number(number):
	exponent = 0
	if number > 1000:
		while number > 10:
			number /= 10
			exponent += 1
		if number == 10:
			number /= 10
			exponent += 1
	return f"{int(number*1000)/1000} e{exponent}"


pygame.init()
Clock = pygame.time.Clock()
smallfont = pygame.freetype.SysFont('Arial', 15)
bigfont = pygame.freetype.SysFont('Arial', 18)
screen = pygame.display.set_mode((720, 720))
how_many_buy = 1
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
color_upgrade1 = (0, 255, 255)
dollaridoos = 0
scripts = Boughtables(0, 0, 1, 1, 0, 0)
lazy_devs = Boughtables(0, 0, 1, 1.07, 0, 10)
dev_teams = Boughtables(0, 0, 1, 1.14, 0, 100)
computing_firms = Boughtables(0, 0, 1, 1.21, 0, 1000)
width = screen.get_width()
height = screen.get_height()
pygame.display.set_caption("IdleGame")
text, rect = smallfont.render("Scripts++, Cost:Free", (0, 0, 0))
text3, rect = smallfont.render("Lazy devs upgrade *2, Cost: 10000", (0, 0, 0))
t1, rect = bigfont.render("1x", (0, 0, 0))
t2, rect = bigfont.render("10x", (0, 0, 0))
t3, rect = bigfont.render("100x", (0, 0, 0))
t4, rect = bigfont.render("1000x", (0, 0, 0))
clear = Rect(40, 40, 300, 200)
up_ld_cost = 10000
up_ld_bought = 0
time_delta = 0
placeholders_total, rect = smallfont.render(f'{scripts} scripts', (0, 255, 255))
while True:
	dt = Clock.tick(30)
	up_ld_cost = int(up_ld_bought * exp(up_ld_bought) * 10000) + 10000
	text0, rect = smallfont.render(f"{big_number(dollaridoos)} Dollaridoos", (255, 0, 255))
	text1, rect = smallfont.render(f"Lazy_devs++, Cost: {big_number(lazy_devs.cost_buy(how_many_buy))} ", (0, 0, 0))
	text2, rect = smallfont.render(f"Dev_teams++, Cost: {big_number(dev_teams.cost_buy(how_many_buy))} ", (0, 0, 0))
	text3, rect = smallfont.render(f"Lazy devs upgrade *2, Cost: {big_number(up_ld_cost)}", (0, 0, 0))
	text4, rect = smallfont.render(f"Computing_firms++, Cost: {big_number(computing_firms.cost_buy(how_many_buy))}", (0, 0, 0))
	placeholders_total, rect = smallfont.render(f'{big_number(scripts.ammount)} scripts', (0, 255, 255))
	lazy_devs_total, rect = smallfont.render(f'{big_number(lazy_devs.ammount)} lazy_devs', (0, 255, 255))
	unfinished_projects_total, rect = smallfont.render(f'{big_number(dev_teams.ammount)} dev_teams', (0, 255, 255))
	overly_ambitious_leaders_total, rect = smallfont.render(f'{big_number(computing_firms.ammount)} computing_firms', (0, 255, 255))
	pygame.draw.rect(screen, (0, 0, 0), clear)
	screen.blit(placeholders_total, (50, 70))
	screen.blit(lazy_devs_total, (50, 90))
	screen.blit(unfinished_projects_total, (50, 110))
	screen.blit(overly_ambitious_leaders_total, (50, 130))
	screen.blit(text0, (50, 50))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if 400 <= mouse[0] <= 450 and 10 <= mouse[1] <= 60:
				how_many_buy = 1            
			if 460 <= mouse[0] <= 510 and 10 <= mouse[1] <= 60:
				how_many_buy = 10
			if 520 <= mouse[0] <= 570 and 10 <= mouse[1] <= 60:
				how_many_buy = 100
			if 580 <= mouse[0] <= 630 and 10 <= mouse[1] <= 60:
				how_many_buy = 1000
			if width / 2 + 40 <= mouse[0] <= (width / 2) + 240 and height / 2 - 10 <= mouse[1] <= height / 2 + 40:
				scripts.ammount += 10
			if width / 2 + 40 <= mouse[0] <= (width / 2) + 260 and height / 2 + 30 <= mouse[1] <= height / 2 + 60:
				if dollaridoos >= lazy_devs.cost_buy(how_many_buy):
					dollaridoos -= lazy_devs.cost_buy(how_many_buy)
					lazy_devs.total_bought += how_many_buy
					lazy_devs.ammount += how_many_buy
			if width / 2 + 40 <= mouse[0] <= (width / 2) + 330 and height / 2 + 70 <= mouse[1] <= height / 2 + 100:
				if dollaridoos >= dev_teams.cost_buy(how_many_buy):
					dollaridoos -= dev_teams.cost_buy(how_many_buy)
					dev_teams.total_bought += how_many_buy
					dev_teams.ammount += how_many_buy
			if width / 2 - 300 <= mouse[0] <= (width / 2) - 40 and height / 2 - 10 <= mouse[1] <= height / 2 + 20:
				if dollaridoos >= up_ld_cost:
					lazy_devs.power *= 2
					up_ld_bought += 1
					dollaridoos -= up_ld_cost
			if width / 2 + 40 <= mouse[0] <= (width / 2) + 330 and height / 2 + 110 <= mouse[1] <= height / 2 + 140:
				if dollaridoos >= computing_firms.cost_buy(how_many_buy):
					dollaridoos -= computing_firms.cost_buy(how_many_buy)
					computing_firms.total_bought += how_many_buy
					computing_firms.ammount += how_many_buy

	time_delta += dt
	if time_delta > 1000:
		dollaridoos += scripts.ammount * scripts.power
		scripts.ammount += lazy_devs.power * lazy_devs.ammount * (2**int(lazy_devs.total_bought / 10))
		scripts.ammount += dev_teams.power * dev_teams.ammount * (2**int(dev_teams.total_bought / 10))
		scripts.ammount += computing_firms.power * computing_firms.ammount * (2**int(computing_firms.total_bought / 10))
		time_delta = 0
	mouse = pygame.mouse.get_pos()
	pygame.draw.rect(screen, (0, 255, 255), [width / 2 + 40, height / 2 - 10, 200, 30])
	pygame.draw.rect(screen, (0, 255, 255), [width / 2 + 40, height / 2 + 30, 220, 30])
	pygame.draw.rect(screen, (0, 255, 255), [width / 2 + 40, height / 2 + 70, 290, 30])
	pygame.draw.rect(screen, color_upgrade1, [width / 2 - 300, height / 2 - 10, 260, 30])
	pygame.draw.rect(screen, color_upgrade1, [width / 2 + 40, height / 2 + 110, 300, 30])
	pygame.draw.rect(screen, color_upgrade1, [400, 10, 50, 50])
	pygame.draw.rect(screen, color_upgrade1, [460, 10, 50, 50])
	pygame.draw.rect(screen, color_upgrade1, [520, 10, 50, 50])
	pygame.draw.rect(screen, color_upgrade1, [580, 10, 50, 50])
	screen.blit(text, (width / 2 + 50, height / 2))
	screen.blit(text1, (width / 2 + 50, height / 2 + 40))
	screen.blit(text2, (width / 2 + 50, height / 2 + 80))
	screen.blit(text3, (width / 2 - 290, height / 2))
	screen.blit(text4, (width / 2 + 50, height / 2 + 120))
	screen.blit(t1, (400, 25))
	screen.blit(t2, (460, 25))
	screen.blit(t3, (520, 25))
	screen.blit(t4, (580, 25))
	pygame.display.update()
