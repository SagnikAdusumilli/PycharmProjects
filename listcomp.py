# list comprehensions are shorcut for forloops
# condesing looping into a single line
grades = [72,82,77,84]
print(grades)
# increment all the grades by 5
grades = [grade+5 for grade in grades]
print(grades)

words = ['NOW', 'IS', 'THE' , 'TIME', 'TO', 'LIVE']
print(words)
words = [word.lower() for word in words]
print(words)

# list comprehensions for files getting data and storing them in a list
grades = [grade.rstrip() for grade in open('grades.txt')]
print(grades)