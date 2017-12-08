# ask for number
answer = int(input('secret number (1-10)? '))

# default guess
guess = 5
while True:
	# get feedback
	feedback = input('is it ' + str(guess) + ' (h/l/Y)? ')
	
	# adjust guess
	if feedback == 'h':
		guess = guess // 2
	elif feedback == 'l':
		guess = guess + (10 - guess) // 2
	# celebrate
	else:
		print('booyah')
		break
