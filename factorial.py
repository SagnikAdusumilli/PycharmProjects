print("enter a number")
num = int(input())
product = 1

for i in range(1, num+1):
	product = product * i
print("factorial is: " + str(product))