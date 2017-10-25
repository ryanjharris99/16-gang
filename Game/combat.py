from gameparser import *

import player
import time
from infectionChance import zombieAttack

def attack(command): #The function that allows the player to attack the zombies
	
	for item in player.inventory: #Check if the item to attack with is in the inventory
		for com in command:
			if(com == item["id"]):
				return item["damage"] #Get the damage attributed to the item

	type_print("Thats not an item you can use.")#If the item doesn't exist or not entered
	type_print("You punch the zombie instead!")
	return 1

def run(command):
    if(random.randint(1, 40) >= 20): #A random chance to see if the player can run away from the zombie
        type_print("You manage to run away")
        return -1 #Successful
    else:
        type_print("You couldn't run so you punched the zombie instead")
        return 1 #Unsuccessful

list_of_combat_functions = {"attack": attack, "hit": attack, "run": run, "escape": run}
def execute_combat_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    Except these commands are specific to combat, essentially creating another game loop
    """
    #Very similar to main game
    if 0 == len(command):
        return

    for key in list_of_combat_functions:
        if(command[0] == key):
            return list_of_combat_functions[key](command)

def menu():

	#Print what the player can do

	type_print("You can:")
	type_print("HIT the zombie with an item.")
	type_print("RUN away.")

	type_print("What do you want to do?")
	
	# Read 	player's input
	print()
	user_input = input("> ")
	print()

    # Normalise the input
	normalised_user_input = normalise_input(user_input)

	return normalised_user_input


def combat(dificulty, zombieHP):
	if(dificulty == "easy"): #Depending on the difficulty, do more damage
		damage_modifier = 0.5
		starting_damage_number = 2
	elif(dificulty == "normal"):
		damage_modifier = 1
		starting_damage_number = 5
	else:
		damage_modifier = 1.5
		starting_damage_number = 7
	type_print("A zombie has appeared!")
	#ASCII art of the zombie 
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

	saved_zombie_hp = zombieHP #Get the hp of the zombie
	players_turn = False #Set the turn order

	while saved_zombie_hp > 0: #While the zombie is alive
		if(players_turn == False):#Zombie's turn
			type_print("Zombie Attacks!")
			player.infected = zombieAttack("bite") #Use the zombieAttack function from infectionChance, determine if the player is infected
			player.player_hp -= random.randint(starting_damage_number, 10) * damage_modifier  #Hurt the player
			type_print("Your health is now: " + str(player.player_hp))
			if(player.player_hp <= 0): #If the player is dead
				type_print("You were defeated!")
				break
			players_turn = True
		else: #player's turn

			print_inventory_items(player.inventory) #print the items available to fight with
			command = menu() #Get the user's input
			damage = execute_combat_command(command)

			if(damage == -1): #If damage = -1 then the user has run away successfully
				break
			elif(damage != None): #If damage is existent
				if(damage < 10):
					type_print("You hit the zombie with the item for: " + str(damage) + " hp") 
				else:
					type_print("You Shoot the zombie !BANG!")
				
				saved_zombie_hp -= damage #Damage the zombie
				player.energy -= 1 #Use 1 of the player's energy
				type_print("Zombies HP is now: " + str(saved_zombie_hp))
				players_turn = False #Start the zombies turn

	if (saved_zombie_hp <= 0): #If the zombies has died
		type_print("The Zombie was defeated")

