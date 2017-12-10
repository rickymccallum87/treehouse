import os
import random

# draw the grid
CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
        (0,1), (1,1), (2,1), (3,1), (4,1),
        (0,2), (1,2), (2,2), (3,2), (4,2),
        (0,3), (1,3), (2,3), (3,3), (4,3),
        (0,4), (1,4), (2,4), (3,4), (4,4)]

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


# limit player movement to map dimensions
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


def draw_map(player):
    print(' _' * 5)
    tile = '|{}'

    for cell in CELLS:
        x, y = cell
        # print(x,y,cell)
        if x < 4:
            line_end = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)


def game_loop():
    # set start positions
    player, monster, door = get_locations()

    while True:
        draw_map(player)
        valid_moves = get_moves(player)
        print('You\'re currently in room {}'.format(player))
        print('You can move {}'.format(', '.join(valid_moves)))
        print('Enter QUIT to quit')

        move = input('> ').lower()
        if move == 'quit':
            break
        # good? change pos
        if move in valid_moves:
            player = move_player(player, move)

            # win/loss condition
            if player == monster:
                clear_screen()
                print('You encountered the monster and were eaten!')
                break
            if player == door:
                clear_screen()
                print('You escaped the dungeon unharmed. Well done!')
                break

        # bad? don't change
        else:
            input('''There's a wall there!''')

        clear_screen()


# introduction
clear_screen()
print('Welcome to the dungeon!')
input('Press return to start!')
clear_screen()
game_loop()
