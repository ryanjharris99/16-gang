from items import *
from map import rooms

infected = False 
inventory = [item_patients_gown, item_parachute]
energy = 10 #The energy level of the player
moved = True #Did the player move room last turn
player_hp = 50 
# Start game at the reception
current_room = rooms["Patient_Room"]
