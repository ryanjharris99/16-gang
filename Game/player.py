from items import *
from map import rooms

inventory = [item_patients_gown]
energy = 10 #The energy level of the player
moved = True #Did the player move room last turn

# Start game at the reception
current_room = rooms["Patient_Room"]
