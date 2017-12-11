import os
import random

dungeon = []
moves = ['left', 'right', 'up', 'down']


# build user specified dungeon size
def create_map(size):
    global dungeon
    for i in range(size):
        for j in range(size):
           dungeon.append((j, i))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# pick random starting locations
def get_locations():
    return random.sample(dungeon, 3)


# take movement input
def move_player(player, move):
    # get location
    x, y = player['location']

    # translate user input into movement tuple
    moveset = {'left': (-1, 0),
              'right': ( 1, 0),
                 'up': ( 0,-1),
               'down': ( 0, 1)}

    # move right/left (x) or up/down (y)
    return x+moveset[move][0], y+moveset[move][1]


# limit player movement to map dimensions
def get_moves(player, map_size):
    moves = ['left', 'right', 'up', 'down']
    x, y = player['location']
    # bound moves between 0 and 4
    if x == 0:
        moves.remove('left')
    if x == map_size - 1:
        moves.remove('right')
    if y == 0:
        moves.remove('up')
    if y == map_size - 1:
        moves.remove('down')
    return moves


def draw_map(player, map_size):
    print(' _' * map_size)
    tile = '|{}'

    for cell in dungeon:
        x, y = cell
        if x < map_size - 1:
            line_end = ''
            if cell == player['location']:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player['location']:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)


def game_loop():
    # allow player to size map
    map_size = int(input('How long is each side of the dungeon? '))
    create_map(map_size)
    clear_screen()
    player = {'location': (0,0), 'visited': []}

    # set start positions
    player['location'], monster, door = get_locations()

    input(player)

    while True:
        draw_map(player, map_size)
        valid_moves = get_moves(player, map_size)
        print('You\'re currently in room {}'.format(player['location']))
        print('You can move {}'.format(', '.join(valid_moves)))
        print('Enter QUIT to quit')

        move = input('> ').lower()
        if move == 'quit':
            break
        # good? change pos
        if move in valid_moves:
            player['location'] = move_player(player, move)

            # win/loss condition
            if player['location'] == monster:
                clear_screen()
                print('You encountered the monster and were eaten!')
                break
            if player['location'] == door:
                clear_screen()
                print('You escaped the dungeon unharmed. Well done!')
                break

        # bad? don't change
        else:
            global moves
            if move in moves:
                input('There\'s a wall there!')
            else:
                input('Movement not recognized')

        clear_screen()


# introduction
clear_screen()
print('Welcome to the dungeon!')
input('Press return to start!')
clear_screen()
game_loop()
