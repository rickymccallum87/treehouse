# randomize
import random
answer = random.randint(1,10)

# allow replay
def game():
	count = 0
	while True:
		
		# limit guesses
		count += 1
		if count > 5:
			print('out of guesses')
			break

		while True:
			# ask
			try:
				guess = int(input('Guess? '))
			# catch non-ints
			except ValueError:
				print('int pls')
			else:
				break


		# compare
		if guess == answer:
			print('yep!')
			break
		# give hint
		elif guess < answer:
			print('too low')
		elif guess > answer:
			print('too high')

while True:
	game()
	play = input('play again(y/n)? ')
	if play != 'y':
		break
