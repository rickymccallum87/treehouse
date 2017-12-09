# add to desired index with .insert()
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
	for i in items:
		print(i)
	
def add(item):
	items.append(item)
	display()
	print('{} added. {} items total'.format(item, len(items)))

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
		add(item)

display()
