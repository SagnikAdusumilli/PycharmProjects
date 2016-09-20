def factorial(number):
	if number <= 1:
		return number
	else: 
		return number * factorial(number-1)

print("Enter a number")
num = int(input())
print(str(num)+"! = "+str(factorial(num)))