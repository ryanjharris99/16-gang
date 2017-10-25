from items import *
from gameparser import *
import player
global inventory
global hp

def checkEndings(current_room, command):
	if current_room["name"] == "Attic" and command[0] == "jump":
		if item_parachute in player.inventory:
			parachuteSurvive(True, False)
			return True

		else:
			parachuteDie(False, False)
			return True
	if player.player_hp <= 0:
		died()
		return True


def parachuteSurvive(survived, infected):
	type_print("You jump from the attic and survive!")

def died():
	type_print("You have died!")

def receptionEnding():
	type_print("""You leave the reception and you’re greeted by the blinding light of day, a light you thought you’d never see. 
		You tall fences all surrounding the hospital. You then spot police lights flashing behind those fences,
		 you stagger towards the lights exhausted from the happenings within the derelict hospital. 
You are greeted at the fence by police officers clothed in massive yellow suits with the writing “BIOHAZARD” all over them.
 One of the men asked whilst looking astonished: “Where did you come from?”
  You are grabbed forcefully by the men and a sample of your blood is taken. 
  Several seconds pass with the man gazing at the device he’s using to examine your blood. 
 The machine beeps and…
""")

	if player.infected == True:
		type_print(""" The officer’s face drops and he goes for his gun. """)
		choice = input("What do you do? (Run/Attack/Scream)")
		type_print("Whilst attempting to " + choice + """way the officer unsheathes his weapon and places it between your eyes before uttering the words:
		 “I’m so sorry.” 
		 BANG. 
		 You came so close but so far.
		 You Die.


  ________                                                 ._.
 /  _____/_____    _____   ____     _______  __ ___________| |
/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \ |
\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/\|
 \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   __
        \/     \/      \/     \/                   \/       \/
""") 

	else:
		type_print("The officer smiles and says “He’s clean. Patch him up and get him some water, he’s been through a lot…”")
		print(""" 
_____.___.               __      __.__         ._.
\__  |   | ____  __ __  /  \    /  \__| ____   | |
 /   |   |/  _ \|  |  \ \   \/\/   /  |/    \  | |
 \____   (  <_> )  |  /  \        /|  |   |  \  \|
 / ______|\____/|____/    \__/\  / |__|___|  /  __
 \/                            \/          \/   \/
""")


