#outFile = open("out.txt","w")
#outFile.write("this is line 1\n")
#outFile.write("this is line 2\n")
# python creates a buffer and writes data on the buffer
# only upon closing the buffer data is transferred
#outFile.close()
#print("data was written")

outFile = open('grades.txt', 'w')
grades = "0"
print("enter a grade (q to quit)")
grades = raw_input()
while (grades != 'q'):
	outFile.write(grades+"\n")
	print("enter a grade (q to quit)")
	grades = raw_input()
outFile.close()


 