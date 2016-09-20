# lambda expressions create anonymus functions

#square = lambda x: x*x
#print(square(2))

numbers = [1,2,3,4]
numbers = list(map(lambda x: x*x, numbers))
print(numbers)