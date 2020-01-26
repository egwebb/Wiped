import pygame, sys
from pygame.locals import *

DISP = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Wiped")
FPS = 60

select = pygame.image.load("megaman.png")
slime = pygame.image.load("Slime_Upscaled_v2.png")
background = pygame.image.load("darknessmyonlyfriend.png")

def spriteLoad():
	if megaX < 290:
		megaX += 60
	else:
		if idle == True:
			megaY += 2
			if megaY > 60:
				idle = False
		else:
			megaY -= 2
			if megaY < 40:
				idle = True


def buttonSelect():
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

def main():
	
	megaX = 50
	megaY = 50

	idle = False
	
	selectX = 200
	selectY = 200

	while True:
		DISP.blit(background, (0,0))
		DISP.blit(slime, (megaX, megaY))
		DISP.blit(select, (selectX, selectY))
		

		for event in pygame.event.get():
			pygame.display.update()

			# if event.type == MOUSEBUTTONDOWN:

			buttonSelect()
			# if event.type == QUIT:
			# 	pygame.quit()
			# 	sys.exit()
			# if event.type == KEYDOWN:
			# 	if event.key == K_DOWN:
			# 		selectY = 50
			# 	if event.key == K_UP:
			# 		selectY = 20
			# 	if event.key == K_RIGHT:
			# 		selectX = 50
			# 	if event.key == K_LEFT:
			# 		selectX = 20

		spriteLoad()			
		# if megaX < 290:
		# 	megaX += 60
		# else:
		# 	if idle == True:
		# 		megaY += 2
		# 		if megaY > 60:
		# 			idle = False
		# 	else:
		# 		megaY -= 2
		# 		if megaY < 40:
		# 			idle = True

		pygame.display.update()
		pygame.time.wait(FPS)

main()
"""
title screen begins with description of where character is
fade opens with decision to make
	menu box
		question
		answer 1
		answer 2
		
user will click on answer
50/50 chance for a monster to appear
	if monster appears
		enter loop
			menu box
				reaction 1 - attack
				reaction 2 - dodge
				reaction 3 - sweep
				monster will attack in return
			exit loop once monsters health is 0
	if not
		move to next decision
after 3 decisions move to boss
		menu box
			reaction 1 - attack
			reaction 2 - dodge
			reaction 3 - sweep
			boss will attack in return
			boss cannot be killed
			boss kills you
game will restart

"""