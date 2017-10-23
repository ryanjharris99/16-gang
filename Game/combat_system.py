import random
# from player import *
import player as player




# def hitted_by_zombies():
#     health =  health -





def easy_mode():
    damages = random.randint(5,10)
    hitdamages = damages * 0.5
    if (player.health > 0) :
        player.health = player.health - hitdamages
    else:
        print("You died !")
    return player.health


def normal_mode():
    damages = random.randint(15,20)
    hitdamages = damages * 1
    if (player.health > 0) :
        player.health = player.health - hitdamages
    else:
        print("You died !")
    return player.health



def hard_mode():
    damages = random.randint(21,30)
    hitdamages = damages * 2
    if (player.health > 0) :
        player.health = player.health - hitdamages
    else:
        print("You died !")
    return player.health


def mode_chosen():
    """ There are three mode and you can chose the mode that you want to play."""
    mode = input("Chose your mode : ")

    if (mode == "0"):
        em = easy_mode()
        print(em)
        mode = em
    elif (mode == "1"):
        nm = normal_mode()
        print(nm)
    elif (mode == "2"):
        hm = hard_mode()
        print(hm)

    while player.health > 0:
           print(easy_mode())



# mode_chosen()


def main():
    while True:
          mode_chosen()

main()

