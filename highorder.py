def square(number):
	return number*number

def isEven(num):
	return (num % 2)==0

def sum(x,y):
	return x+y

# map takes a function and a sequence of data and applies it to the function
numbers = [1,2,3]
print(numbers)
numbers = list(map(square, numbers))
print(numbers)

# filter is the same as map except it works with boolean function
# it is used to filter the data from a list that makes the function true
numbers = list(range(1,11))
print(numbers)
numbers = list(filter(isEven, numbers))
print(numbers)

#reduce takes a list and applies a reduces it to a result of a function
import functools
numbers = list(range(1,11))
sum = functools.reduce(sum, numbers)
print(sum)


