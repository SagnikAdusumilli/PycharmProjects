# a function is an ojbect like any other objects in python
def square(number):
    return number * number


# assigning function to a vairable
sqnumber = square
num = sqnumber(2)
print(num)

# map = highe-order function (calls another function as an argument)
# map takes 2 ojbects: function and data sequence
# it applies the function to the data sequence
numbers = [1, 2, 3, 4]
numbers = list(map(square, numbers))
# numbers = [square(i) for i in numbers]
print(numbers)
