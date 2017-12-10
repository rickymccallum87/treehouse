import random

def game():
    answer = random.randint(1,10)
    attempts = 5

    while attempts:

        while True:
            try:
                guess = int(input('> '))
                break
            except ValueError:
                print('Guess a whole number.')

        if guess == answer:
            print('You win!')
            break
        else:
            attempts -= 1
            if guess < answer:
                print('Too low.')
            else:
                print('Too high.')

    else:
        print('You lose!')

game()

while True:
    again = input('Play again (Y/n)? ')
    if again != 'n':
        print('New game!')
        game()
    else:
        print('Goodbye.')
        break
