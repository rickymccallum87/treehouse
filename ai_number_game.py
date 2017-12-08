# ask for number
answer = int(input('secret number (1-10)? '))

# possible range
between = [1,10]
while True:
	# think out loud
	print('between ' + str(between[0]) + ' and ' + str(between[1]) + '..')

	# guess
	guess = (between[0] + between[1]) // 2

	# get feedback
	feedback = input('is it ' + str(guess) + ' (h/l/Y)? ')
	
	# adjust guess
	if feedback == 'h':
		between[1] = guess - 1
	elif feedback == 'l':
		between[0] = guess + 1
	# celebrate
	else:
		print('booyah')
		break
