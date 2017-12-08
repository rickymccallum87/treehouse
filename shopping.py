items = []

def instruct():
	print('Create your shopping list.')
	print(
'''These commands are supported:
done > print list and quit
show > print list and continue
help > see these instructions''')

def display():
	for i in items:
		print(i)
	
while True:
	item = input('New item? ')
	if item == 'done':
		break
	# show to print current list
	elif item == 'show':
		display()
	# help to print instructions
	elif item == 'help':
		instruct()
	else:
		items.append(item)

display()
