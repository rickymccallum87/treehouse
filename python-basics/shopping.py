import os

items = []

# clear screen on update
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def instruct():
	clear()
	print('Create your shopping list.')
	print(
'''These commands are supported:
done > print list and quit
show > print list and continue
help > see these instructions''')

def display():
	clear()
	index = 1
	for item in items:
		print('{}- {}'.format(index, item))
		index += 1
	print('\'' * 20)
	
def add(item):
	display()
	if items:
		pos = input('{} goes where?\n> '.format(item))
	else:
		pos = 0
	
	try:
		pos = abs(int(pos))
	except ValueError:
		pos = None
		items.append(item)
	else:
		items.insert(pos-1, item)

	display()
	
	print('{} added. {} items total'.format(item, len(items)))

while True:
	item = input('> ')
	if item == 'done':
		break
	# show to print current list
	elif item == 'show':
		display()
	# help to print instructions
	elif item == 'help':
		instruct()
	else:
		add(item)

display()
