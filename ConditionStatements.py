print("enter the number of hours worked: ")
hoursWorked = int(raw_input())
rate = 25.00
if (hoursWorked >40):
	grossPay = (40*rate) + ((hoursWorked - 40)*(rate*1.5))
else:
	grossPay = hoursWorked*rate
print("Gross pay: "+ str(grossPay))

print("Enter a numeric grade: ")
grade = int(raw_input())
if grade >= 90:
	letterGrade = "A"
elif grade >= 80: 
	letterGrade = "B"
elif grade >= 70:
	letterGrade = "C"
elif grade >= 60:
	letterGrade = "D"
else:
	letterGrade = "F"
print("letter grade is: "+letterGrade)