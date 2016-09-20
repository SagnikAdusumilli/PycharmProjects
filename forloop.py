# version 1 used for interating through lists
names = ["Sagnik", "Riju", "Random"]
for name in names:
	print name
# access by indexing
numbers = [1,2,3,4,5,6,7,8,9,10]
print("getting all the even numbers in the list")
for i in range(0, len(numbers)+1, 2):
	print(i)
# version 2: iterating through touples
numbers = (1,2,3,4,5)
sum =0
for num in numbers:
	sum = sum + num
	print(num)
print("sum: "+ str(sum))

words = ("now","is", "the", "time")
max = 0
for i in range(0, len(words)):
	if len(words[i]) > len(words[max]):
		max = i
print("The longest word is: "+ words[max])

# version 3: dictionaries
dict = {"Cynthia": 96,"Raymond": 92, "David":100}
for key in dict.keys():
	print("KEY: "+ key+" "+ str(dict[key]))
