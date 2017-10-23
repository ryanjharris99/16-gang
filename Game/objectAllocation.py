#This program returns where the object will be randomly spawaned ina  list of places
from random import randint
from map import rooms
from player import *
from items import *
from gameparser import *
from timeFunction import *
import time
import sys

def keyAlreadyExists(dictionary, testKey):
	toReturn = False

	for key in dictionary:
		#print(key)
		if key == testKey:
			toReturn = True

	return toReturn


def dictToLongList (dictionaryList):
	dictlist = []
	for key, value in dictionaryList.items():
		temp = [key,value]
		dictlist.append(temp)

	return dictlist

def longListSimple (longList):
	shortList = []
	for i in range (0, len(longList)):
		shortList.append(longList[i][0])

	return shortList

def dictToListFull (toConvert):

	workingWith = dictToLongList(toConvert)
	workingWith = longListSimple(workingWith)

	return (workingWith)


def allocateLocation (listOfPlaces):
	"""This takes a list of places that teh user can search through.
	It then returns one of these places where teh object will be put."""
	listLength = len(listOfPlaces) 							#gets the length of the list 
	randomInteger = randint(0, listLength-1)					#creates a random integer

	return listOfPlaces[randomInteger] 						#returns one of the rooms

def itemsToAllocate (items, places):
	"""This function takes a list of items and a list of places.
	"""
	itemMap = {}
	itemDict = {}

	for i in range (0, len(items)):
		itemDict = {}

		itemToPlace = items[i]
		itemAllocatedPlace = allocateLocation(places)
		print("The " + itemToPlace + " is in " + itemAllocatedPlace + ".")

		if keyAlreadyExists(itemMap, itemAllocatedPlace) == False:

			itemDict["0"] = [itemToPlace]

			itemMap[itemAllocatedPlace] = itemDict

		else: 
			dictionaryLength = len(itemMap[itemAllocatedPlace])

			itemDict[str(dictionaryLength)] = [itemToPlace]
			
			itemMap[itemAllocatedPlace][i] = itemDict


	print()
	return itemMap


def itemsToContainers (roomName):
	for i in range(0, len(rooms[roomName]["items"])):
		hidingplacesList = dictToListFull(rooms[roomName]["containers"])
		roomSelected = allocateLocation(hidingplacesList)
		#print(roomSelected)
		rooms[roomName]["containers"][roomSelected].append(rooms[roomName]["items"][i])



def initiateRooms ():

    roomsList = dictToListFull(rooms)    

    for i in range (0, len(roomsList)):
        itemsToContainers(roomsList[i])

    #print(rooms["OT"]["containers"])

def listWhatsWhere(amount, names):
    toReturn = " "

    for i in range(0, len(names)):
        toReturn = (names[i]["name"]) + ","

    return toReturn


def displayContainerItems (room):
    for i in rooms[room]["containers"]:
        print (("In " + i + " there is: " + listWhatsWhere(len(rooms[room]["containers"][i]),rooms[room]["containers"][i]) + ".").lower())



"""examplePlaces = ["Left Cuboard","Right Cuboard","Desk Drawer", "Under Body",]

itemsToPlace = ["Parachute Craft List", "Knife", "Cheese Pasty"]

searchItem = examplePlaces[0]


while True:				

	print()
	input("Press Enter ")
	print()
	dictionaryVersion = itemsToAllocate(itemsToPlace, examplePlaces)
	print()
	print(dictionaryVersion)
	print()
	searchItem = input("Where would you like to search: ").title()
	try:
		print()
		print(dictionaryVersion[searchItem])
	except: 
		print("Nothing in the " + searchItem + ".")"""




	
	

