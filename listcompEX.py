# storing even numbers i a list
N = range(1, 101)
list = [x for x in N if x % 2 == 0]
print(list)

# print the length of all the words in a sentence
sent = "now is the time to learn python"
sent = sent.split(" ")
words = [(word, len(word)) for word in sent]

# sorting acording to increasing order
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[j][1] < words[i][1]:
            temp = words[j]
            words[j] = words[i]
            words[i] = temp
for word in words:
    print(word)
