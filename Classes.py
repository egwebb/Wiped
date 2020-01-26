#Encounter
class Encounter:
    def __init__(self, enemy, hero)
        self.turn = 0
        self.result = False
        self.enemy = enemy
        self.hero = hero

#Main Class
class Character:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.options = ["attack", "dodge", "sweep"]

#Enemy
class Enemy(Character):
    def __init__(sprite):
        self.sprite = sprite

class Hero(Character):
    pass

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