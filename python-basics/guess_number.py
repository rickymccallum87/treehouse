import random

answer = random.randint(1,10)

while True:
    guess = int(input('> '))

    if guess == answer:
        print('That\'s right!')
        break
    else:
        print('Wrong.')
