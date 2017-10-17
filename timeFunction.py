#This is the function which returns a time and can be used to 
import time 



def getCurrentTime ():
	"""This function returns the time as a Float.
	It will be useful for time critical incidents.
	For example time in the xRay machine.
	Or time whilst fighting the zombies."""
	return time.time()


initTime = getCurrentTime() #this would be then time you enter x-ray room

while True:
	input ("press Enter: ")
	currentTime = getCurrentTime()         #updates the current time
	timeSinceInit = currentTime - initTime #this calcualtes the time since initial event
	print(timeSinceInit)				   #prints the time
