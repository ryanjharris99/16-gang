#used this website https://automatetheboringstuff.com/chapter15/
import time 
import random

#This file is used to store time functions, and since many more can be added in future, it is a suitable decomposition

def xrayRoomMessage ():
#https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
	Messages = ["You're starting to feel drowsy...", "Your Hands are starting to sweat...","Something doesn't feel right...","You start to feel weak..."]
	return(random.choice(Messages)) #Return a random message from the list of messages


def getCurrentTime ():
	"""This function returns the time as a Float.
	It will be useful for time critical incidents.
	For example time in the xRay machine.
	Or time whilst fighting the zombies."""
	return time.time() #Get the current time

def timeSince(initial, current):
	return current - initial #Work out the time since two events
