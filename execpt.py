print("Enter a numerator:")
numer = int(input())
print("Enter a denominator:")
denom = int(input())
try:
	quotient = numer / denom
	print(quotient)
except ZeroDivisionError:
	print("division by 0")

 