from items import *
from game import *
global inventory

def checkEndings(current_room, command):
	if current_room["name"] == "Attic" and command[0] == "jump":
		if item_parachute in inventory:
			parachuteSurvive()
			return True

		else:
			parachuteDie()
			return True


def parachuteSurvive():
	print("You jump from the attic and survive!")


def parachuteDie():
	print("You have jumped from the window and died.")
