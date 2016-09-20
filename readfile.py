count =0
total =0
inFile = open('grades.txt','r')
grade = inFile.readline()
# checking null
while (grade):
	print(grade)
	count = count+1
	total= total + int(grade)
	grade = inFile.readline()
average = total/count
print("average: "+ str(average))