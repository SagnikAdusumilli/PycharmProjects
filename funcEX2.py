# this program creats an acrynom for a sentence

def first (word):
	return word[0].upper()

def acronym(words):
	acro = ''
	acro = acro.join(list(map(first, words)))
	return acro

words = ['in','my','humble','opinion']
print(acronym(words))
