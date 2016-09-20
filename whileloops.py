#summation count controlled loop
sum = 0
number = 1
print("enter the range summation range")
target = int(raw_input())
while number <= target:
	sum = sum + number
	number = number +1
print("sum is: " + str(sum))

#event control loop
print("event controled loop")
average = 0.0
total = 0.0
count = 0
print("enter a grade (-1 to quit)")
grade = float(raw_input())
while -1 != grade:
	total = total + grade
	count = count + 1
	print("enter a grad (-1 to quit)")
	grade = float(raw_input())
average = total/count
print("Average grade: "+ str(average))	

# use of continue
numer =0
denom = 0
while denom !=-1 and numer !=-1:
	print("Enter a numerator")
	numer = float(raw_input())
	print("Enter a denominator")
	denom = float(raw_input())
	if denom==0:
		continue
	print(str(numer/denom))
# use of break
number =0
total =0
average =0.0
count =0
while True:
	print("enter a number: ")
	number = int(raw_input())
	if number == -1:
		break
	total = number + total
	count = count+1
average = total/count
print("Average: "+ str(average))