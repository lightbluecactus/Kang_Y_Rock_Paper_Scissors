from gameComponents import gameVars


# define a win or lose function
# things inside function are like in a box.
def winorloss(status):

	# print("inside winorloss function; status is: ", status)
	print("you", status, "! Would you like to play again?")
	# choice is going to change every time, so there's no need to connect it with gameVars
	choice = input("Y / N\n")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit()

	elif choice == "Y" or choice == "y":
		# reset the player lives and the ai lives
		# and set player to False so that our loop will restart
		# "global" tells the function scope to find these 3 variables outside the function, thus the variables are connected.
		# global player_lives 

		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False

	# this still has a bug

	else:
		print("Make a valid choice - Y or N\n")
		# this will generate a bug that we need to fix later
		choice = input("Y / N")

# end of the function