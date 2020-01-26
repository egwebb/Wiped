import pygame, sys
from pygame.locals import *

def buttonSelect(event, selectX, selectY, vertical, horizontal):

	if event.type == QUIT:
		pygame.quit()
		sys.exit()
	if event.type == KEYDOWN:
		if event.key == K_DOWN:
			vertical = 2
			selectY = 400
		if event.key == K_UP:
			vertical = 1
			selectY = 300
		if event.key == K_RIGHT:
			horizontal = 2
			selectX = 400
		if event.key == K_LEFT:
			horizontal = 1
			selectX = 200
		if event.key == K_RETURN:
			if vertical == 1 and horizontal == 1:
				print("up, left")
			if vertical == 1 and horizontal == 2:
				print("up, right")
			if vertical == 2 and horizontal == 1:
				print("bottom, left")
			if vertical == 2 and horizontal == 2:
				print("bottom, right")
	return selectX, selectY, vertical, horizontal

def spriteLoad(X, Y, idle, slime):
	if X < 290:
		X += 60
	else:
		if idle == True:
			if Y > 55:
				slime = pygame.image.load("assets\Slime_Upscaled_Squished_v2.png")
				# slime = pygame.image.load("assets\Skeleton_Upscaled_v2.png")
				Y += 1
			else:
				Y += 3
			if Y > 60:
				idle = False
		else:
			slime = pygame.image.load("assets\Slime_Upscaled_v2.png")
			Y -= 15
			if Y < 40:
				idle = True
	return X, Y, idle, slime
