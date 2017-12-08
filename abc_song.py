abc = list('abcdefghijklmnopqrstuvwxyz')

# slice with -1 step to reverse
cba = abc[::-1]

# sing function for cadence
def sing(alpha):
	for i in alpha:
		# current spot
		th = alpha.index(i)

		print(i, end='')

		if th == 6 or th == 18 or th == 21 or th == 23:
			print(', ', end='')
		elif th > 10 and th < 15:
			print('-', end='')
		elif th == 15:
			print('. ', end='')
		elif th == 24:
			print(' and ', end='')
		else:
			print(' ', end='')
			
	print('\n')

# sing abc's forward and backward
sing(abc)
sing(cba)
