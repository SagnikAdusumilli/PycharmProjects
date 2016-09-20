sentence = "now is the time for all good people to come"
sentence += " to the aid of their party"
words = sentence.split(" ")
words = sorted(words)
print(words)
numWords = {}
for i in range(0,len(words)):
	if words[i] in numWords:
		numWords[words[i]] += 1
	else:
		# the word is put in the dictionary if it dosen't exist
		numWords[words[i]] = 1
print("counted list")
for key in numWords.keys():
	print(key, numWords[key])