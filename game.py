# set up a container with our choices inside, and let the AI pick one randomly
# pick a package to generate numbers
from random import randint
from gameComponents import gameVars, chooseWinner, checkResults

# remember to make EVERYTHING under indent
# same as while player == False
while gameVars.player is False:

	print("\n=============///* RPS GAME *///=============")
	print("Computer Lives: ", gameVars.ai_lives, "/", gameVars.total_lives)
	print("Player Lives: ", gameVars.player_lives, "/", gameVars.total_lives)
	print("- - - - - - - - - - - - - - - - - - - - - - ")

	# \n means "new line"
	print("Choose your weapon! or type quit to exit\n")

	# this is the player choice
	# "Pick rock, paper, or scissors: " is a prompt
	# player = is creating a variable
	gameVars.player = input("Pick rock, paper, or scissors:\n")

	# player has a value, so it's true now.

	# if the player chose to quit, then exit the game
	# == means compare the left (player) and right ("quit")
	if gameVars.player == "quit":
		print("you chose to quit")
		exit()

	# this will be the AI choice
	# generate a random number, and the number reflects the three options.
	computer = gameVars.choices[randint(0,2)]

	# validate that the input worked 
	# print means showing the result
	print("\nPlayer chose: " + gameVars.player)
	# validate that the random choice worked for the ai
	print("AI chose: " + computer, '\n' )


	checkResults.comparison(computer)

	if gameVars.player_lives is 0:
		chooseWinner.winorloss("lost")

	if gameVars.ai_lives is 0:
		chooseWinner.winorloss("won")

			# select all those lines and hit ctrl+/ to comment all
			# the lines below are moved into function (see chooseWinner.py)
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

	print("- - - - - - - - - - - - - - - - - - - - - - ")
	print("player has", gameVars.player_lives, "lives left")
	print("AI has", gameVars.ai_lives, "lives left\n")

	# set player back to false to keep it running in loop
	gameVars.player = False