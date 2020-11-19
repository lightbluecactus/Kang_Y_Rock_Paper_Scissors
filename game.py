# set up a container with our choices inside, and let the AI pick one randomly
# pick a package to generate numbers
from random import randint

#an array is a datatype in nerd-speak ==> arrays are 0-based
# every entry gets an index
# this is all of the three options.
choices = ["rock", "paper", "scissors"]

# give our player and AI some lives
player_lives = 5
ai_lives = 5

# true and false are boolean data types -> the equivalent of 1 and 0
player = False

# remember to make everything under indence
# same as while player == False
while player is False:

	# this is the player choice
	# input("Pick rock, paper, or scissors: ") is a prompt
	# my_choice = is creating a variable
	player = input("Pick rock, paper, or scissors: ")

	# player has a value, so it's true now.

	# this will be the AI choice
	# generate a random number, and the number reflects the three options.
	computer = choices[randint(0,2)]

	# valdate that the input worked 
	# print means showing the result
	print("Player chose " + player)
	#validate that the random choice worked for the ai
	print("AI chose: " + computer)

	# check to see who won or if it's a tie
	if (computer == player):
		print("tie")
		# always check for negative conditions first (the losing case)

	elif (computer == "rock"):
		if (player == "scissors"):
			print("you lose!")
			# take a life away from the player
			player_lives = player_lives - 1 

			# could also be player_lives -= 1 for short

		else:
			print("you won!")
			# take a life away from the ai
			ai_lives = ai_lives - 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!")
			player_lives = player_lives - 1
		else:
			print("you won!")
			ai_lives = ai_lives - 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!")
			player_lives = player_lives - 1
		else:
			print("you won!")
			ai_lives = ai_lives - 1

	print("player has", player_lives, "lives left")
	print("AI has", ai_lives, "lives left")

	# set player back to false to keep it running in loop
	player = False