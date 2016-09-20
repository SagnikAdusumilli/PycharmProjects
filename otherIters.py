#iterators for range
numbers = range(1,11)
it = iter(numbers)
print(next(it))
# os is an interface for interacting with the operating system
import os
files = os.popen('dir *.py')
for file in files:
	print(file)
