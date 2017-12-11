import os, random

# Build list of (x, y) coordinates
def create_map(size, dungeon):
    for i in range(size):
        for j in range(size):
           dungeon.append((j, i))

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Randomize unique starting positions
def get_locations(dungeon):
    return random.sample(dungeon, 3)

# Show current state of dungeon grid
def draw_map(dungeon, player, monster, map_size):
    print(' _' * map_size)
    tile = '|{}'
    for cell in dungeon:
        x, y = cell
        if x < map_size - 1:
            line_end = ''
            if cell == player['location']:
                output = tile.format('X')
            elif cell == monster:
                output = tile.format('!')
            elif cell in player['visited']:
                output = tile.format('.')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player['location']:
                output = tile.format('X|')
            elif cell == monster:
                output = tile.format('!|')
            elif cell in player['visited']:
                output = tile.format('.|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)

# Stop player from moving through walls
def get_moves(player, map_size):
    moves = ['left', 'right', 'up', 'down']
    x, y = player['location']
    if x == 0:
        moves.remove('left')
    if x == map_size - 1:
        moves.remove('right')
    if y == 0:
        moves.remove('up')
    if y == map_size - 1:
        moves.remove('down')
    return moves

# Move relative to current position
def move_player(player, move):
    x, y = player['location']
    moveset = {'left': (-1, 0),
              'right': ( 1, 0),
                 'up': ( 0,-1),
               'down': ( 0, 1)}
    return x+moveset[move][0], y+moveset[move][1]

# Move monster within map bounds, including diagonally
def move_monster(monster, map_size):
    x = random.randint(-1,1)
    y = random.randint(-1,1)
    x += monster[0]
    y += monster[1]
    if x > map_size-1:
        x = map_size-1
    if y > map_size-1:
        y = map_size-1
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    return x, y

# Main game
def game():
    
    # Initialize new game
    dungeon = []
    map_size = int(input('How long is each side of this dungeon?\n> '))
    create_map(map_size, dungeon)
    clear()
    player = {'location': (0,0), 'visited': []}
    player['location'], monster, door = get_locations(dungeon)
    player['visited'].append(player['location'])
    
    # Gameplay loop
    while True:
        
        # Show current state
        draw_map(dungeon, player, monster, map_size)
        valid_moves = get_moves(player, map_size)
        
        # Ask player for move
        print('You\'re currently in room {}'.format(player['location']))
        print('You can move {}'.format(', '.join(valid_moves)) + ' or (Q)uit')
        move = input('> ').lower()
        
        # Quit
        if move == 'q':
            return
        
        # Accept player's move
        if move in valid_moves:
            player['location'] = move_player(player, move)
            player['visited'].append(player['location'])
            
            # Collision with other elements
            if player['location'] == monster:
                clear()
                print('You encountered the monster and were eaten!')
                return False # Report lost
            if player['location'] == door:
                clear()
                print('You escaped the dungeon unharmed!')
                return True # Report won
            
        # Invalid move command
        else:
            if move in ['left', 'right', 'up', 'down']:
                input('There\'s a wall there!\n')
            else:
                input('Movement not recognized.\n')
         
        # Monster's turn to move
        monster = move_monster(monster, map_size)
        clear()

# Welcome
clear()
print('Welcome to the dungeon!')
scoreboard = [0,0] # [wins, losses]

# Play multiple games
while True:
    print('Wins: ' + str(scoreboard[0]) + ' Losses: ' + str(scoreboard[1]))
    won = game()
    if won:
        again = input('Congratulations! Play again (Y/n)?\n> ')
        scoreboard[0] += 1
    elif won == None:
        print('Goodbye.')
        break
    else:
        again = input('Oh well. Play again (Y/n)?\n> ')
        scoreboard[1] += 1
    if again == 'n':
        print('Goodbye.')
        break
    clear()
    print('You daringly enter another dungeon!')

# Display final result
print('Wins: ' + str(scoreboard[0]) + ' Losses: ' + str(scoreboard[1]))
