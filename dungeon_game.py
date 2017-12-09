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
	# move right/left (x) or up/down (y)
	return player

# move player, within bounds
def get_moves(player):
	moves = ['left', 'right', 'up', 'down']
	# bound moves between 0 and 4
	return moves

player, monster, door = get_locations()
while True:
	print('Welcome!')
	print('You\'re currently in room {}') # format player pos
	print('You can move {}') # format available moves
	print('Enter QUIT to quit')

	move = input('> ').lower()
	
	if move == 'quit':
		break

	# good? change pos
	# bad? don't change
	# on door? win!
	# on monster? lose!
	# else loop


