import player
import time
from gameparser import type_print
from game import main
def print_title():
	print(""" .-. .-. .---.    .---. ,---.  ,-. _______  .--.  ,-.      _____   
 | | | |/ .-. )  ( .-._)| .-.\ |(||__   __|/ /\ \ | |     /___  /  
 | `-' || | |(_)(_) \   | |-' )(_)  )| |  / /__\ \| |        / /)  
 | .-. || | | | _  \ \  | |--' | | (_) |  |  __  || |       / /(_) 
 | | |)|\ `-' /( `-'  ) | |    | |   | |  | |  |)|| `--.   / /___  
 /(  (_) )---'  `----'  /(     `-'   `-'  |_|  (_)|( __.' (_____/  
(__)    (_)            (__)                       (_)            \n""")

def print_main_menu():
	type_print("START - Begin the horrors\n")
	type_print("INFO - What the game is and how to play ")

def print_info():
	type_print("ADD GAME INFO HERE")
	type_print("BACK - Back to main menu")

def print_difficulty():
	type_print("EASY - You won't have any trouble")
	type_print("NORMAL - You will face a challenge")
	type_print("HARD - Good luck")

def main_menu():
	current_menu = "main_menu"
	print_title()
	while True:
		if current_menu == "main_menu":
			print_main_menu()
			user_input = input("> ").lower()
			if user_input == "start":
				current_menu = "difficulty"
			elif user_input == "info":
				current_menu = "info"
			else:
				type_print("What?")
		if current_menu == "info":
			print_info()
			user_input = input("> ").lower()
			if user_input == "back":
				current_menu = "main_menu"
			else:
				type_print("What?")
		if current_menu == "difficulty":
			print_difficulty()
			user_input = input("> ").lower()
			if user_input == "easy":
				player.difficulty = "easy"
				print("\n" * 100)
				introduction()
				break
			elif user_input == "normal":
				player.difficulty = "normal"	
				print("\n" * 100)
				introduction()
				break
			elif user_input == "hard":
				player.difficulty = "hard"
				print("\n" * 100)
				introduction()
				break
			else:
				type_print("What?")

def introduction():
	intro_list = ["You come to life with a splutter, air pouring into your lungs.","You manage to gain control of your breathing.","You don't remember anything, where are you?",
					"What happened?", "You look around and see you are in a hospital bed.", "All of the machines and lights are off, something seems off.",
					"Surely someone would have at least rushed past the door...","Where is everyone?", "You struggle to sit up, but you need to look around.",
					"You stumble onto your feet, you need to find out what has happened."]
	for items in intro_list:
		type_print(items, 0)
		time.sleep(0)
	main()

def print_game_over():
	print("""
	  ________                                                 ._.
	 /  _____/_____    _____   ____     _______  __ ___________| |
	/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \ |
	\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/\|
	 \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   __
	        \/     \/      \/     \/                   \/       \/
	""")