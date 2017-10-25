#chance of infection
from random import uniform


diffMult = {"easy": 0.5, "normal": 1, "hard": 2}
difficulty = diffMult["normal"]

def zombieAttack (typeOfAttack):

	attackTypes = {"scratch": 0.5, "bite": 2}

	chance = 1 * difficulty * attackTypes[typeOfAttack]

	odds = 10

	randomInteger = uniform(0, odds)
	print(randomInteger)

	if randomInteger <= chance:
		return True #player has been infected

	else:
		return False


while True:
	input()
	if zombieAttack("bite") == True:
		print("You feel an intense burn coming from within your veins themselves...")



	