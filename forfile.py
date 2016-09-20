# for loop works on a sequence of data
# a file is nothing more than a sequence of data
for line in open("grades.txt"):
	print(line, end = "")