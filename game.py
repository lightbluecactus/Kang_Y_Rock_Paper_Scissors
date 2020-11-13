# set up a container with our choices inside, and let the AI pick one randomly
# pick a package to generate numbers
from random import randint

#an array is a datatype in nerd-speak ==> arrays are 0-based
# every entry gets an index
# this is all of the three options.
choices = ["rock", "paper", "scissors"]

# computer is our AI opponent - let it make a choice
# generate a random number, and the number reflects the three options.
computer = choices[randint(0,2)]

# give the user some weapon options
# input("Pick rock, paper, or scissors: ") is a prompt
# my_choice = is creating a variable
player = input("Pick rock, paper, or scissors: ")

# valdate that the input worked 
# print means showing the result
print("Player chose " + player)
print("AI chose: " + computer)

# check to see who won or if it's a tie
if (computer == player):
	print("tie")
	#reset the game loop and have the user choose again

elif (computer == "rock"):
	if (player == "scissors"):
		print("you lose!")
		# take a life away from the player
	else:
		print("you won!")
		# take a life away from the player

elif (computer == "paper"):
	if (player == "rock"):
		print("you lose!")
		# take a life away from the player
	else:
		print("you won!")
		# take a life away from the player

elif (computer == "scissors"):
	if (player == "paper"):
		print("you lose!")
		# take a life away from the player
	else:
		print("you won!")
		# take a life away from the player