numbers = [1,2,3]
# creating explicit iterator
it = iter(numbers)
#printing the current pointer
print(next(it))
print(next(it))
print(next(it))
# file objects are setup as iterators
fileIt = open("grades.txt", 'r')
print(next(fileIt))