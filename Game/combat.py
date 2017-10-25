from gameparser import *

import player
import time

def attack(command):
	
	for item in player.inventory:
		for com in command:
			if(com == item["id"]):
				return item["damage"]

	type_print("Thats not an item you can use")
	type_print("you punch the zombie instead!")
	return 1

def run(command):
    if(random.randint(1, 40) >= 20):
        type_print("you manage to run away")
        return -1
    else:
        type_print("you couldn't run so you punched the zombie instead")
        return 1

list_of_combat_functions = {"attack": attack, "hit": attack, "run": run, "escape": run}
def execute_combat_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if 0 == len(command):
        return

    for key in list_of_combat_functions:
        if(command[0] == key):
            return list_of_combat_functions[key](command)

def menu():

	type_print("You can HIT the zombie with an item")

	type_print("You can RUN away")

	type_print("What do you want to do?")
	
	# Read 	player's input
	print()
	user_input = input("> ")
	print()

    # Normalise the input
	normalised_user_input = normalise_input(user_input)

	return normalised_user_input


def combat(dificulty, zombieHP):
	if(dificulty == "easy"):
		damage_modifier = 0.5
		starting_damage_number = 2
	elif(dificulty == "normal"):
		damage_modifier = 1
		starting_damage_number = 5
	else:
		damage_modifier = 2
		starting_damage_number = 10
	type_print("A zombie has appeared!!!")

	print(""" 

                               |_|_|_|
                               C C  /            
                              /<   /             
               ___ __________/_#__=o             
              /(- /(\_\________   \              
              \ ) \ )_      \o     \             
              /|\ /|\       |'     |             
                            |     _|             
                            /o   __\             
                           / '     |             
                          / /      |             
                         /_/\______|             
                        (   _(    <              
                         \    \    \             
                          \    \    |            
                           \____\____\           
                           ____\_\__\_\          
                         /`   /`     o\          
                         |___ |_______|.
                       	""")

	saved_zombie_hp = zombieHP
	players_turn = False

	while saved_zombie_hp > 0:
		if(players_turn == False):
			type_print("zombie Attacks!")
			player.player_hp -= random.randint(starting_damage_number, 10) * damage_modifier 
			type_print("your health is now: " + str(player.player_hp))
			if(player.player_hp <= 0):
				type_print("You were defeated!")
				break
			players_turn = True
		else:

			print_inventory_items(player.inventory)
			command = menu()
			damage = execute_combat_command(command)

			if(damage == -1):
				break
			else:
				if(damage < 10):
					type_print("You hit the zombie with the item for: " + str(damage) + " hp")
				else:
					type_print("You Shoot the zombie !BANG!")
				
				saved_zombie_hp -= damage
				player.energy -= 1
				type_print("Zombies HP is now: " + str(saved_zombie_hp))
				players_turn = False

	if (saved_zombie_hp <= 0):
		type_print("The Zombie was defeated")

