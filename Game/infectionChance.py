#chance of infection
from random import uniform
import player

diffMult = {"easy": 0.5, "normal": 1, "hard": 2} #Higher chance of being infected on harder difficulties
difficulty = diffMult[player.difficulty] #Get the float representing the difficulty

#This file is used to check if the player has been infected when hit

def zombieAttack (typeOfAttack):

	attackTypes = {"scratch": 0.5, "bite": 2} #

	chance = 1 * difficulty * attackTypes[typeOfAttack] #Work out the chance of being infected

	randomInteger = uniform(0, 10) #Get a number between 1 and 10

	if randomInteger <= chance: #If the random number is larger than the chance of infection
		return True #player has been infected

	else:
		return False #The player is okay
	