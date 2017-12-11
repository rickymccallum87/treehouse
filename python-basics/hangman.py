import random

# randomly select from list of words
words = ['cat', 'dog', 'hen', 'pie', 'bull']
answer = words[random.randint(0, len(words) - 1)]
# print(answer) # debug

# track errors and guesses
errors = 0
guesses = []

while True:
	won = True

	# guess
	guess = input('guess? ')

	if guess in answer:
		# record correct guess
		guesses.append(guess)

		# show progress
		for char in answer:
			if char in guesses:
				print(char, end='')
			else:
				won = False
				print('_', end='')
		print('\n', end='')
		# win condition
		if won:
			print('well done!')
			break
	else:
		errors += 1
		print('nope. ' + str(errors) + ' wrong guesses')
		if errors > 5:
			print('you lose')
			break

