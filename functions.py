import pygame, sys
from pygame.locals import *

def spriteLoad(megaX, megaY, idle):
	if megaX < 290:
		megaX += 60
	else:
		if idle == True:
			slime = pygame.image.load("assets\Slime_Upscaled_v2.png")
			megaY += 2
			if megaY > 60:
				idle = False
		else:
			slime = pygame.image.load("assets\Slime_Upscaled_Squished_v2.png")
			megaY -= 2
			if megaY < 40:
				idle = True
	return megaX, megaY, idle


def buttonSelect(event, selectX, selectY):
	if event.type == QUIT:
		pygame.quit()
		sys.exit()
	if event.type == KEYDOWN:
		if event.key == K_DOWN:
			selectY = 50
		if event.key == K_UP:
			selectY = 20
		if event.key == K_RIGHT:
			selectX = 50
		if event.key == K_LEFT:
			selectX = 20
	return selectX, selectY
