# set up a container with our choices inside, and let the AI pick one randomly
# pick a package to generate numbers
from random import randint
from gameComponents import gameVars, chooseWinner

# remember to make EVERYTHING under indent
# same as while player == False
while gameVars.player is False:

	print("===============*/ RPS GAME */===============")
	print("Computer Lives: ", gameVars.ai_lives, "/", gameVars.total_lives)
	print("Player Lives: ", gameVars.player_lives, "/", gameVars.total_lives)
	print("============================================")

	# \n means "new line"
	print("Choose your weapon! or type quit to exit\n")

	# this is the player choice
	# input("Pick rock, paper, or scissors: ") is a prompt
	# my_choice = is creating a variable
	gameVars.player = input("Pick rock, paper, or scissors: \n")

	# player has a value, so it's true now.

	# if the player chose to quit, then exit the game
	# == means compare the left (player) and right ("quit")
	if gameVars.player == "quit":
		print("you chose to quit")
		exit()

	# this will be the AI choice
	# generate a random number, and the number reflects the three options.
	computer = gameVars.choices[randint(0,2)]

	# valdate that the input worked 
	# print means showing the result
	print("Player chose " + gameVars.player)
	#validate that the random choice worked for the ai
	print("AI chose: " + computer)

	# ------MOVE THIS CHUNK OF CODE TO A PACKAGE - STARTS HERE--------

	# check to see who won or if it's a tie
	if (computer == gameVars.player):
		print("tie")
		# always check for negative conditions first (the losing case)

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose!")
			# take a life away from the player
			gameVars.player_lives -= 1 
			# player_lives -= 1 for short
			# player_lives = player_lives -1 for longer

		else:
			print("you won!")
			# take a life away from the ai
			gameVars.ai_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("you lose!")
			gameVars.player_lives -= 1
		else:
			print("you won!")
			gameVars.ai_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose!")
			gameVars.player_lives -= 1
		else:
			print("you won!")
			gameVars.ai_lives -= 1

	# ---------STOP HERE - ALL OF THE ABOVE NEEDS TO MOVE--------

	if gameVars.player_lives is 0:
		chooseWinner.winorloss("lost")

	if gameVars.ai_lives is 0:
		chooseWinner.winorloss("won")

			# select all those lines and hit ctrl+/ to comment all
			# the lines below are moved into function (see winORlose.py)
		# print("you won! Would you like to play again?")
		# choice = input("Y / N\n")

		# if choice == "N" or choice == "n":
		# 	print("You chose to quit! Good luck next time!")
		# 	exit()

		# elif choice == "Y" or choice == "y":
		# 	# reset the player lives and the ai lives
		# 	# and set player to False so that our loop will restart
		# 	player_lives = 1
		# 	ai_lives = 1
		# 	player = False

		# else:
		# 	print("Make a valid choice - Y or N\n")
		# 	# this will generate a bug that we need to fix later
		# 	choice = input("Y / N")

	print("player has", gameVars.player_lives, "lives left")
	print("AI has", gameVars.ai_lives, "lives left")

	# set player back to false to keep it running in loop
	gameVars.player = False