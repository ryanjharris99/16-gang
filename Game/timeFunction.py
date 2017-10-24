#used this website https://automatetheboringstuff.com/chapter15/
import time 
import random


def main ():
	initial = getCurrentTime ()

	difficult = 1
	"""
	if (difficulty == "easy"):
		difficult = 1
	elif (difficulty == "medium"):
		difficult == 1.5

	elif (difficulty == "hard"):
		difficult == 2

	"""

	for i in range (4):
		printMessage()
		time.sleep(15*difficult)

	
	print("Oh no! you stayed too long inside the room, you couldnt survive...")	
	

	


def printMessage ():
#https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
	Messages = ["You're starting to feel drowsy...", "You're Hands are starting to sweat...","something doesn't feel right...","You can start to feel weak..."]
	print(random.choice(Messages))


def getCurrentTime ():
	"""This function returns the time as a Float.
	It will be useful for time critical incidents.
	For example time in the xRay machine.
	Or time whilst fighting the zombies."""
	return time.time()

def timeSince(initial):
	current = getCurrentTime()

	print (current)

	print (initial)

	return current - initial

main ()