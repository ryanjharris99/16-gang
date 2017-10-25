from items import *
from gameparser import *
import player
global inventory
global hp

def checkEndings(current_room, command):
	if current_room["name"] == "Attic" and command[0] == "jump":
		if item_parachute in player.inventory:
			parachuteSurvive(True, False)
			return True

		else:
			parachuteDie(False, False)
			return True
	if player.player_hp <= 0:
		died()
		return True


def parachuteSurvive(survived, infected):
	type_print("You jump from the attic and survive!")

def died():
	type_print("You have died!")


