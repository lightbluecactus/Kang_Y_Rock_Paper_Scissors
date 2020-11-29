from gameComponents import gameVars

def comparison(computer):

	# check to see who won or if it's a tie
	if (computer == gameVars.player):
		print(">>>>> TIE")

		# always check for negative conditions first (the losing case)
	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print(">>>>> YOU LOSE!")
			# take a life away from the player
			gameVars.player_lives -= 1 
			# player_lives -= 1 for short
			# player_lives = player_lives -1 for longer

		elif (gameVars.player == "paper"):
			print(">>>>> YOU WON!")
			# take a life away from the ai
			gameVars.ai_lives -= 1

		else:
			print("  ! Please choose from the three weapons!")


	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print(">>>>> YOU LOSE!")
			gameVars.player_lives -= 1
		elif (gameVars.player == "scissors"):
			print(">>>>> YOU WON!")
			gameVars.ai_lives -= 1
		else:
			print("  ! Please choose from the three weapons!")

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print(">>>>> YOU LOSE!")
			gameVars.player_lives -= 1
		elif (gameVars.player == "rock"):
			print(">>>>> YOU WON!")
			gameVars.ai_lives -= 1
		else:
			print("  ! Please choose from the three weapons!")