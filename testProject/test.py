#!/usr/bin/env python

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((500, 500))
ship = pygame.image.load('alien1.png').convert()
background = pygame.image.load('shoes.jpg').convert()
screen.blit(background, (0,0))
#alien = GameObject(image, 71, 5)

class GameObject:
	def __init__(self, image, height, speed):
		self.speed = speed
		self.image = image
		self.pos = image.get_rect().move(0, height)

	def move(self):
		self.pos = self.pos.move(self.speed, 0)
		if self.pos.right > 400:
			self.pos.left = 0

alien = GameObject(ship, 0, 5)

def main():
	going = True
	while going:
		for event in pygame.event.get():
			if event.type == QUIT:
				going = False
		screen.blit(background, alien.pos, alien.pos)
		alien.move()
		screen.blit(alien.image, alien.pos)
		pygame.display.update()
		pygame.time.delay(100)
	
	pygame.quit()

if __name__ == '__main__':
	main()
