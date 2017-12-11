# 1
name = input('Name? ')
while True:
	try:
		year = int(input('Year born? '))
	except ValueError:
		print('i need an integer')
	else:
		break

# 2
quad = [25,50,75,100]

for i in quad:
	if year + i < 2017:
		continue
	print(name + ' will be ' + str(i) + ' in the year ' + str(year + i))
