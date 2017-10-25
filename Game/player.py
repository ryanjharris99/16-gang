from items import *
from map import rooms

infected = False #If the player is infected
inventory = [item_patients_gown] #The player's inventory
energy = 20 #The energy level of the player
moved = True #Did the player move room last turn
player_hp = 50  #The player's HP
difficulty = "easy" #The difficulty (Set to easy by default)
morgue_open = False #IF the morgue has been opened
power_on = False #IF the power is on
current_room = rooms["Patient_Room"] #THe room the player is currently in
