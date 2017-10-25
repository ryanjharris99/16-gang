from items import *
from map import rooms

infected = True
inventory = [item_patients_gown]
energy = 20 #The energy level of the player
moved = True #Did the player move room last turn
player_hp = 50 
difficulty = "easy"
morgue_open = False
power_on = False
# Start game at the reception
current_room = rooms["Patient_Room"]
