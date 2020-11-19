# set up a container with our choices inside, and let the AI pick one randomly
# pick a package to generate numbers
from random import randint

#an array is a datatype in nerd-speak ==> arrays are 0-based
# every entry gets an index
# this is all of the three options.
choices = ["rock", "paper", "scissors"]

# give our player and AI some lives
player_lives = 1
ai_lives = 1

total_lives = 1

# define a win or lose function
# things inside function are like in a box.
def winorloss(status):

	# print("inside winorloss function; status is: ", status)
	print("you", status, "! Would you like to play again?")
	choice = input("Y / N\n")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit()

	elif choice == "Y" or choice == "y":
		# reset the player lives and the ai lives
		# and set player to False so that our loop will restart
		# "global" tells the function scope to find these 3 variables outside the function, thus the variables are connected.
		global player_lives 
		global ai_lives
		global player

		player_lives = 1
		ai_lives = 1
		player = False

	else:
		print("Make a valid choice - Y or N\n")
		# this will generate a bug that we need to fix later
		choice = input("Y / N")


# true and false are boolean data types -> the equivalent of 1 and 0
player = False

# remember to make EVERYTHING under indence
# same as while player == False
while player is False:

	print("===============*/ RPS GAME */===============")
	print("Computer Lives: ", ai_lives, "/", total_lives)
	print("Player Lives: ", player_lives, "/", total_lives)
	print("============================================")

	# \n means "new line"
	print("Choose your weapon! or type quit to exit\n")

	# this is the player choice
	# input("Pick rock, paper, or scissors: ") is a prompt
	# my_choice = is creating a variable
	player = input("Pick rock, paper, or scissors: \n")

	# player has a value, so it's true now.

	# if the player chose to quit, then exit the game
	# == means compare the left (player) and right ("quit")
	if player == "quit":
		print("you chose to quit")
		exit()

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


	if player_lives is 0:
		winorloss("lost")

	if ai_lives is 0:
		winorloss("won")

			# select all those lines and hit ctrl+/ to comment all
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

	print("player has", player_lives, "lives left")
	print("AI has", ai_lives, "lives left")

	# set player back to false to keep it running in loop
	player = False