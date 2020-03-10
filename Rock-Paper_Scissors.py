'''  Simple Rock-Paper-Scissors game.'''


import random


print('\n -----Welcome to ROCK-PAPER-SCISSORS---- \n')


# Game Loop to control game. 
while True:

	# Define opponents (op) possible hands  
	op = ['Rock','Paper','Scissors']

	# Let player chose his hand
	Hand = input('Please Choose a hand: ')

	print('\n\n')
	# Print both the opponent(op) hand and the players input hand
	print(f' {Hand}')
	print('---VS---')
	op = (random.choice(op))
	print(f' {op}')


	# Check for all possible winning scanarios
	if op[0].lower() == Hand[0].lower():
		print('\nDRAW!\n')

	if Hand[0].lower() == 'r' and op[0].lower() == 'p':
		print('\nPaper Wins!\n')

	if op[0].lower() == 'r' and Hand[0].lower() == 'p':
		print('\nPaper Wins!\n')

	if Hand[0].lower() == 's' and op[0].lower() == 'r':
		print('\nRock Wins!\n')

	if op[0].lower() == 's' and Hand[0].lower() == 'r':
		print('\nRock Wins!\n')

	if Hand[0].lower() == 'p' and op[0].lower() == 's':
		print('\nScissors Wins!\n')

	if op[0].lower() == 'p' and Hand[0].lower() == 's':
		print('\nScissors Wins!\n')

	
	# Ask to play agian and only break out of game loop if answer is no 
	play_again = input('Would you like to play agian: ')

	if play_again[0].lower() == 'n':
		break 
		

print('\nThanks for palying!\n')



