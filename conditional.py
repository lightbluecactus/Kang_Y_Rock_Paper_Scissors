# set up a variable, check its value, and then do sth. different depending on the outcome

# cast our user input - which by default will be text - to a number using int()

temperature = int(input("input a value between 0 and 100: "))

# compare user input with some conditions
if (temperature <= 4):
	# water is frozen
	print("water is solid frozen!")
elif (temperature < 100):
	#water is liquid
	print("liquid!")
else:
	#water is boiling (above 100 degrees)
	print("water is vapor")
