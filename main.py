from functions import *

DISP = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Wiped")
FPS = 60

def main():
	vertical = 2
	horizontal = 2

	skeleton = pygame.image.load("assets\Skeleton_Upscaled_v2.png")
	select = pygame.image.load("assets\Square.png")
	slime = pygame.image.load("assets\Slime_Upscaled_v2.png")
	# slime = pygame.image.load("assets\Skeleton_Upscaled_v2.png")
	background = pygame.image.load("assets\\battlemenu_blank_original.png")		
	blackground = pygame.image.load("assets\\black.png")
	X = 250
	Y = 480
	selectX = 400
	selectY = 375
	idle = False
	updateXY = ()
	updateButton = ()
	
	while True:
		DISP.blit(blackground, (0, 0))
		DISP.blit(background, (0, 240))
		DISP.blit(slime, (X, Y))
		DISP.blit(select, (selectX, selectY))
		
		for event in pygame.event.get():
			pygame.display.update()
			updateButton = buttonSelect(event, selectX, selectY, vertical, horizontal)
			(selectX, selectY, vertical, horizontal) = updateButton

		updateXY = spriteLoad(X, Y, idle, slime)
		(X, Y, idle, slime) = updateXY

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