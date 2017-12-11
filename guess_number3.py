def game():
    print('Think of a number between 1 and 10.')
    while True:
        try:
            attempts = int(input('How many tries do I get?\n> '))
        except ValueError:
            print('Give me a whole number.')
        else:
            if attempts < 1:
                print('I need at least one chance.')
                continue
            else:
                break
    print('(H)igher, (L)ower, (Y)es')
    poss = [1,10]

    while attempts:
        guess = int((poss[0] + poss[1]) // 2)
        print('Is it ' + str(guess) + '?')
        response = input('> ')
        if response == 'y':
            print('I win!')
            break
        else:
            if response == 'h':
                print('Higher..')
                poss[0] = guess + 1
            elif response == 'l':
                print('Lower..')
                poss[1] = guess - 1
            else:
                print('I don\'t understand.')
                continue
        if poss[0] > poss[1]:
            print('You cheated!')
            return True
        attempts -= 1
    else:
        print('I lose!')


while True:
    cheated = game()
    if cheated:
        break
    again = input('Play again (Y/n)? ')
    if again != 'n':
        print('New game!')
    else:
        print('Goodbye.')
        break
