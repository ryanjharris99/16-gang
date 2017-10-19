from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
energy = 20 #The energy level of the player
moved = True #Did the player move room last turn

# Start game at the reception
current_room = rooms["Reception"]
