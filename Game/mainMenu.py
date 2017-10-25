import player
import time
import os
from pygame import mixer
from gameparser import type_print
from game import main

mixer.init()
menu_music = mixer.music.load(os.path.dirname(os.path.realpath(__file__)) + "\sounds\menumusic.wav") #The music to be played in the menu

def print_title(): #ASCII title of the game
	print(""" .-. .-. .---.    .---. ,---.  ,-. _______  .--.  ,-.      _____   
 | | | |/ .-. )  ( .-._)| .-.\ |(||__   __|/ /\ \ | |     /___  /  
 | `-' || | |(_)(_) \   | |-' )(_)  )| |  / /__\ \| |        / /)  
 | .-. || | | | _  \ \  | |--' | | (_) |  |  __  || |       / /(_) 
 | | |)|\ `-' /( `-'  ) | |    | |   | |  | |  |)|| `--.   / /___  
 /(  (_) )---'  `----'  /(     `-'   `-'  |_|  (_)|( __.' (_____/  
(__)    (_)            (__)                       (_)            \n""")

def print_main_menu(): #Print the main menu
	type_print("START - Begin the horrors\n")
	type_print("INFO - What the game is and how to play ")

def print_info():#Info about the game if that option is chosen
	type_print("HOSPITAL Z is a text-based horror survival game.")
	type_print("The aim of the game is to escape the hospital.")
	type_print("This is achieved by typing commands into the program.")
	type_print("The game interprets your commands and will change accordingly.")
	type_print("BACK - Back to main menu")

def print_difficulty():#Difficulty options
	type_print("EASY - You won't have any trouble")
	type_print("NORMAL - You will face a challenge")
	type_print("HARD - Good luck")

def main_menu(): #The main loop for the menu
	mixer.music.play()
	mixer.music.set_volume(0.1)
	current_menu = "main_menu"
	print_title()
	while True:#Until the loop is broken
		if current_menu == "main_menu":#If on the main menu
			print_main_menu()#Print the current menu
			user_input = input("> ").lower()#Take the user input
			if user_input == "start": #Go to whichever menu the user asked for
				current_menu = "difficulty"
			elif user_input == "info":
				current_menu = "info"
			else:
				type_print("What?")
		if current_menu == "info": #Same for all menus, more elegant solution to be added
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
				mixer.music.stop()
				introduction()
				break
			elif user_input == "normal":
				player.difficulty = "normal"	
				print("\n" * 100)
				mixer.music.stop()
				introduction()
				break
			elif user_input == "hard":
				player.difficulty = "hard"
				print("\n" * 100)
				mixer.music.stop()
				introduction()
				break
			else:
				type_print("What?")

def introduction(): #Print the introduction to the game and then start the game
	intro_list = ["You come to life with a splutter, air pouring into your lungs.","You manage to gain control of your breathing.","You don't remember anything, where are you?",
					"What happened?", "You look around and see you are in a hospital bed.", "All of the machines and lights are off, something seems off.",
					"Surely someone would have at least rushed past the door...","Where is everyone?", "You struggle to sit up, but you need to look around.",
					"You stumble onto your feet, you need to find out what has happened."]
	for items in intro_list:
		type_print(items)
		time.sleep(1)#Have a 1 second break between lines so the user can read it and to add dramatic effect
	main()