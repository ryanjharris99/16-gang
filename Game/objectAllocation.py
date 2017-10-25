#This program returns where the object will be randomly spawaned ina  list of places
from random import randint
from map import rooms
from player import *
from items import *
from gameparser import *
from timeFunction import *
import time
import sys

#This file is used to take a list of items and containers and allocate the items into the containers randomly
#This makes the game more interesting as it will be different every time

def keyAlreadyExists(dictionary, testKey): #This function is called if the container already contains an item
	toReturn = False

	for key in dictionary:
		#print(key)
		if key == testKey:
			toReturn = True

	return toReturn


def dictToLongList (dictionaryList): #This takes a dictionary and returns a list
	dictlist = []
	for key, value in dictionaryList.items(): #For each value in the dictionary
		temp = [key,value]
		dictlist.append(temp) #Add it to the list
	return dictlist

def longListSimple (longList): #This function will take a dictionary and return a list of the keys
	shortList = []
	for i in range (0, len(longList)):
		shortList.append(longList[i][0])

	return shortList

def dictToListFull (toConvert):

	workingWith = dictToLongList(toConvert)
	workingWith = longListSimple(workingWith)

	return (workingWith)


def allocateLocation (listOfPlaces):
	"""This takes a list of places that the user can search through.
	It then returns one of these places where teh object will be put."""
	listLength = len(listOfPlaces) 							#gets the length of the list 
	randomInteger = randint(0, listLength-1)					#creates a random integer

	return listOfPlaces[randomInteger] 						#returns one of the rooms

def itemsToAllocate (items, places):
	"""This function takes a list of items and a list of places.
	"""
	itemMap = {}
	itemDict = {}

	for i in range (0, len(items)): #For each item in the list
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

	return itemMap


def itemsToContainers (roomName): #This function takes a roomname and sorts the items into containers in that room, using previously created functions
	for i in range(0, len(rooms[roomName]["items"])):
		hidingplacesList = dictToListFull(rooms[roomName]["containers"])
		roomSelected = allocateLocation(hidingplacesList)
		rooms[roomName]["containers"][roomSelected].append(rooms[roomName]["items"][i])

	rooms[roomName]["items"] = {}

	rooms[roomName]["items"] = []




def initiateRooms (): #The function that uses all other functions and is used in the main game.py

    roomsList = dictToListFull(rooms)    

    for i in range (0, len(roomsList)):
        itemsToContainers(roomsList[i])






	
	

