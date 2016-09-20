#print() prints to the cmd
#cannont contcant number and string

#print() can print out data in the form of a touple
word = "word"
number = 100
print(word, number)

#format string
name = "Mary"
grade = 87.929
format = "%s: %.2f" %(name, grade)
print(format)

#getting input from the user
print("enter a number")
num1 = int(input())
print("enter another number")
num2 = int(input())
print("the sum is: "+ str(num1+num2))

#print re-direction, statements printed onto a different locations

#printing onto a file method 1
file = open("text1.txt", "a")
print >> file,"hello"
print('hello')

#printing onto a file method 2
import sys
sys.stdout = open("text2.txt",'a')
print("hello")




