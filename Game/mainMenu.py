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
	type_print("You come to life with a splutter, air pouring into your lungs.")
	time.sleep(1)
	type_print("You manage to gain control of your breathing.")
	time.sleep(1)
	type_print("You don't remember anything, where are you?")
	time.sleep(1)
	type_print("What happened?")
	time.sleep(1)
	type_print("You look around and see you are in a hospital bed.")
	time.sleep(1)
	type_print("All of the machines and lights are off, something seems off.")
	time.sleep(1)
	type_print("Surely someone would have at least rushed past the door...")
	time.sleep(1)
	type_print("Where is everyone?")
	time.sleep(1)
	type_print("You struggle to sit up, but you need to look around.")
	time.sleep(1)
	type_print("You stumble onto your feet, you need to find out what has happened.")
	main()