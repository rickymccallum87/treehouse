# get word from user
word = list(input('word? '))

vowels = ['a', 'e', 'i', 'o', 'u']

# remove all instances of each vowel
for v in vowels:
	while True:
		try:
			word.remove(v)
		except ValueError:
			break

# print result
print('more like ' + ''.join(word))
