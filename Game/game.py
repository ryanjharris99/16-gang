#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from timeFunction import *
from objectAllocation import *
from mainMenu import *
import time
import sys
import platform
if platform.system() == "Windows":
    import winsound
import os 
dir_sounds = os.path.dirname(os.path.realpath(__file__)) + "\sounds\\"

difficulty = ""


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).
    """

    item_list = ""
    for item in items:
        if item_list != "":
            item_list += ", "
            item_list += item["name"]
        else:
            item_list += item["name"]
    return item_list
        

def print_containers(container):
    """This function prints all of the containers in a given room"""
    type_print("SEARCH the " + container + ".")



def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". 
    """
    items_string = list_of_items(items)
    if items_string != "":
        type_print("INVENTORY:\n")
        for item in items:
            type_print(" - " + item["name"])


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:
    """
    global moved
    # Display room name
    print("\n")
    if moved == True or moved == None: #If the player has moved
        type_print(room["name"].upper())
        # Display room description
        type_print(room["description"])
        moved = False

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.
    """
    type_print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print:

    """
    global energy
    type_print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for container in current_room["containers"]:
        print_containers(container)
    print("")
    if energy > 16:
        type_print("You are full of energy!")
    elif energy > 12:
        type_print("You are feeling okay!")
    elif energy > 8:
        type_print("You are starting to feel tired.")
    elif energy > 4:
        type_print("You are very tired.")
    elif energy > 0:
        type_print("You are about to faint, eat something!")
    #
    # COMPLETE ME!
    #
    
    type_print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    global moved
    exits = (current_room["exits"])
    if is_valid_exit(exits, direction):
        moved = True
        current_room = move(exits, direction)

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    global inventory
    items_room = current_room["items"]
    for item in items_room:
        if item_id == item["id"]:
            inventory.append(item)
            items_room.remove(item)
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    global inventory
    items_room = current_room["items"]
    for item in inventory:
        if item_id == item["id"]:
            inventory.remove(item)
            items_room.append(item)

def execute_read(item_id):
    """This function prints the description of a chosen item in the players inventory"
    """
    global inventory
    items_room = current_room["items"]
    for item in inventory:
        if item_id == item["id"]:
            type_print(item["description"])

def execute_search(container_id):
    """This function searches a given container and adds any items in it to the 
    player's inventory"""
    global inventory
    containers_room = current_room["containers"]
    list_of_containers = []
    to_delete = ""
    for item in containers_room:
        list_of_containers.append(item)
        if container_id == item:
            if len(containers_room[container_id]) != 0:
                for items in current_room["containers"][container_id]:
                    type_print("You found a " + items["name"] + ".\n")
                    inventory.append(items)
            else:
                if item[-1] == "s":
                    type_print("The " + item + " were empty.\n")
                else:
                    type_print("The " + item + " was empty.\n")
            to_delete = item
    if to_delete != "":
        del current_room["containers"][to_delete]
    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            type_print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            type_print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            type_print("Drop what?")
    elif command[0] == "read" or command[0] == "inspect":
        if len(command) > 1:
            execute_read(command[1])
        else:
            type_print(command[0] + " what?")
    elif command[0] == "search":
        if len(command) > 1:
            execute_search(command[1])
        else:
            type_print("Search what?")
    elif command[0] == "combine" or command[0] == "craft":
        if(len(command) > 1):
            user_input = []
            for word in command:
                if word != "combine":
                    user_input.append(word)

            CraftedItem = crafting(finding_crafting_items(user_input))

            if(CraftedItem != None):
                type_print("\n" + "You have crafted: " + CraftedItem["name"])
                global inventory

                inventory.append(CraftedItem)
                foundItems = finding_crafting_items(user_input)
                for item in foundItems:
                    inventory.remove(item)
            else:
                type_print("You can't craft anything with these")
        else:
            type_print("Combine what?")
    else:
        type_print("What?")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")
    print()

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def finding_crafting_items(user_input):
    global inventory

    Items = []

    for word in user_input:
        for item in inventory:
            if (item["id"] == word):
                Items.append(item)


    return Items



def crafting(Items):

    if(len(Items) != 0):
        for item in items_list:

            if(len(item["recipe"]) != 0):


                Item_number = 0
                for item2 in Items:
                    if (item2 in item["recipe"]):
                        Item_number += 1

                if(Item_number == len(item["recipe"])):
                    return item
                


        return None    

    else:
        return None


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction".
    """

    # Next room to go to
    moved = True
    return rooms[exits[direction]]

def type_print(text):
    if platform.system() == "Windows":
        winsound.PlaySound(dir_sounds + "typing.wav" ,winsound.SND_FILENAME | winsound.SND_ASYNC)
    for c in text:
        sys.stdout.write( '%s' % c ) #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")  
    if platform.system() == "Windows":
        winsound.PlaySound(None, winsound.SND_PURGE)


# This is the entry point of our program
def main():
    global energy
    gameStart = getCurrentTime() #time the game started
    energyLossTime = getCurrentTime() #time since energy was last lost
    initiateRooms()

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        if timeSince(energyLossTime, getCurrentTime()) > 60:
            energy -= 1




# Are we being run as a s`ipt? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main_menu()

