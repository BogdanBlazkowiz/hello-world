import pygame
from pygame.locals import *
from math import exp, cos, sin, pi, log1p, acos
import random
import sys
import time

pygame.init()
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), RESIZABLE)
pygame.display.set_caption("Gravity")
width = screen.get_width()
height = screen.get_height()
size_block = 10
objects_list = []
a = pi

def vector_distance(point_1, point_2):
    distance = ((point_2[0]-point_1[0])**2 + (point_2[1] - point_1[1])**2)**0.5
    return distance


class Space_Object:
    def __init__(self, mass, density, position, movement):
        self.mass = mass
        self.radius = self.mass * density
        self.position_x = position[0]
        self.position_y = position[1]
        self.id = time.time()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.velocity = movement
        self.velocity_angle = a
        self.vector2 = (self.velocity*cos(self.velocity_angle), self.velocity*sin(self.velocity_angle))

    def move(self):

        self.position_x += self.vector2[0]/self.mass
        self.position_y += self.vector2[1]/self.mass
        if self.position_x > width or self.position_x < 0:
            self.vector2 = (-1*self.vector2[0], self.vector2[1])

        if self.position_y > height or self.position_y < 0:
            self.vector2 = (self.vector2[0], -1*self.vector2[1])
    def collision(self):
        for f in objects_list:
            if self.id == f.id:
                continue
            else:
                if (vector_distance((self.position_x, self.position_y), (f.position_x, f.position_y))) < (self.radius+f.radius):
                    self.vector2 = (self.vector2[0]*-1, (self.vector2[1]*-1))
    def gravity(self):
        for f in objects_list:

            if self.id == f.id or (self.mass * f.mass)/ ((vector_distance((self.position_x, self.position_y), (f.position_x, f.position_y)))**2)/10 < 0.0005:
                continue
            else:
                force = (self.mass * f.mass)/ ((vector_distance((self.position_x, self.position_y), (f.position_x, f.position_y)))**2)/10
                angle = acos((f.position_x-self.position_x)/(vector_distance((self.position_x, self.position_y), (f.position_x, f.position_y))))
                if f.position_y < self.position_y:
                    angle *= -1
                temp_vector = (force*cos(angle), force*sin(angle))
                self.vector2 = (temp_vector[0]+self.vector2[0], temp_vector[1]+self.vector2[1])
while True:
    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            objects_list.append(Space_Object(81000, 0.001, mouse, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            objects_list.append(Space_Object(10, 1, mouse, 50))
        if pressed[K_SPACE]:
            print("lol")
            objects_list = []
    screen.fill("BLACK")
    for f in objects_list:

        f.gravity()
    for f in objects_list:
        pygame.draw.circle(screen, (0, 0, 0), (f.position_x, f.position_y), f.radius)
        f.collision()
        f.move()
        pygame.draw.circle(screen, f.color, (f.position_x, f.position_y), f.radius)
    pygame.display.update()
    Clock.tick(60)
