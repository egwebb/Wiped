# PyGame template.
 
# Import standard modules.
import sys
import Classes
 
# Import non-standard modules.
import pygame
from pygame.locals import *
 
def update(dt):
  pygame.init()

  """
  Update game. Called once per frame.
  dt is the amount of time passed since last frame.
  If you want to have constant apparent movement no matter your framerate,
  what you can do is something like
  
  x += v * dt
  
  and this will scale your velocity based on time. Extend as necessary."""
  
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():
    # We need to handle these events. Initially the only one you'll want to care
    # about is the QUIT event, because if you don't handle it, your game will crash
    # whenever someone tries to exit.
    if event.type == QUIT:
      pygame.quit() # Opposite of pygame.init
      sys.exit() # Not including this line crashes the script on Windows. Possibly
      # on other operating systems too, but I don't know for sure.
    # Handle other events as you wish.

 
def draw(screen):
  pygame.init()

  """
  Draw things to the window. Called once per frame.
  """
  screen.fill((0, 0, 0)) # Fill the screen with black.
  
  # Redraw screen here.
  
  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()

def combat(heroOption, enemyOption, player, enemy):
  if heroOption == "attack":
    if enemyOption == "attack":
      return "The attacks cancel out!"
    if enemyOption == "sweep":
      enemy.health -= 1
      return "Your attack beats the enemy's sweep!"
    if enemyOption == "dodge":
      player.health -= 1
      return "The enemy has dodged your attack!"
  if heroOption == "sweep":
    if enemyOption == "attack":
      player.health -= 1
      return "Your sweep is foiled by the enemy's attack!"
    if enemyOption == "sweep":
      return "The sweeps cancel out!"
    if enemyOption == "dodge":
      enemy.health -= 1
      return "Your sweep beats the enemy's dodge!" 
  if heroOption == "dodge":
    if enemyOption == "attack":
      enemy.health -= 1
      return "You dodge the enemy's attack!"
    if enemyOption == "sweep":
      player.health -= 1
      return "The enemy catches your dodge with their sweep!"
    if enemyOption == "dodge":
      return "You both dodge!" 

def runPyGame():
  # Initialise PyGame.
  pygame.init()
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 30.0
  fpsClock = pygame.time.Clock()
  
  # Set up the window.
  width, height = 640, 480
  screen = pygame.display.set_mode([width, height])
  
  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
  dt = 1/fps # dt is the time since last frame.

  player = Classes.Hero(10, 1, 5)
  enemy = NULL



  while True: # Loop forever!
    update(dt) # You can update/draw here, I've just moved the code for neatness.
    draw(screen)
    
    dt = fpsClock.tick(fps)
runPyGame()