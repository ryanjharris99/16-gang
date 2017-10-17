#This program returns where the object will be randomly spawaned ina  list of places
from random import randint

def keyAlreadyExists(dictionary, testKey):
	toReturn = False

	for key in dictionary:
		print(key)
		if key == testKey:
			toReturn = True

	return toReturn


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
			
			itemMap[itemAllocatedPlace] = itemDict


	print()
	return itemMap

def dictionaryToList(dict):
	toReturn = []

	for key in dict:
		toReturn.append(dict[key])

	return toReturn



examplePlaces = ["Left Cuboard","Right Cuboard","Desk Drawer", "Under Body",]

itemsToPlace = ["Parachute Craft List", "Knife", "Cheese Pasty"]


while True:				

	print()
	input("Press Enter ")
	print()
	print(itemsToAllocate(itemsToPlace, examplePlaces))




	
	

