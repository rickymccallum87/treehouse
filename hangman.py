# track errors
# allow guesses
# show progress
# win/lose

import random

# randomly select from list of words
words = ['cat', 'dog', 'hen', 'pie', 'bull']
answer = words[random.randint(0, len(words) - 1)]

print(answer)
