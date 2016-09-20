def countLetter(words):
	if len(words)<1:
		return 0
	else: 
		return len(words[0]) + countLetter(words[1:])
sentence = ['now', 'is', 'time', 'the']
print(sentence)
print(countLetter(sentence))

