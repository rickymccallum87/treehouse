import os
import random

# draw player
# check for win/loss
# clear screen and redraw grid

# draw the grid
CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0), 
	 (0,0), (1,1), (2,1), (3,1), (4,1), 
	 (0,0), (1,2), (2,2), (3,2), (4,2), 
	 (0,0), (1,3), (2,3), (3,3), (4,3), 
	 (0,0), (1,4), (2,4), (3,4), (4,4)]

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

# pick random starting locations
def get_locations():
	return random.sample(CELLS, 3)

# take movement input
def move_player(player, move):
	# get location
	x, y = player

	# translate user input into movement tuple
	moveset = {'left': (-1, 0),
		   'right': ( 1, 0),
		      'up': ( 0,-1),
		    'down': ( 0, 1)}

	# move right/left (x) or up/down (y)
	return x+moveset[move][0], y+moveset[move][1]

# move player, within bounds
def get_moves(player):
	moves = ['left', 'right', 'up', 'down']
	x, y = player
	# bound moves between 0 and 4
	if x == 0:
		moves.remove('left')
	if x == 4:
		moves.remove('right')
	if y == 0:
		moves.remove('up')
	if y == 4:
		moves.remove('down')
	return moves

def game_loop():
	player, monster, door = get_locations()

	while True:
		valid_moves = get_moves(player)
		clear_screen()
		print('You\'re currently in room {}'.format(player))
		print('You can move {}'.format(', '.join(valid_moves)))
		print('Enter QUIT to quit')

		move = input('> ').lower()
		
		if move == 'quit':
			break
		# good? change pos
		if move in valid_moves:
			player = move_player(player, move)
		# bad? don't change
		else:
			input('''There's a wall there!''')

clear_screen()
print('Welcome to the dungeon!')
input('Press return to start!')
clear_screen()
game_loop()
