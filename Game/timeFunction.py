#This is the function which returns a time and can be used to 
import time 



def getCurrentTime ():
	"""This function returns the time as a Float.
	It will be useful for time critical incidents.
	For example time in the xRay machine.
	Or time whilst fighting the zombies."""
	return time.time()

def timeSince(initial, current):
	return current - initial
