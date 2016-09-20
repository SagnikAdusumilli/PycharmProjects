class Name:
	# python does not require you to define the feilds first
	# constructor
	# self refers to the current instance of the class (this)
	def __init__(self,first, middle, last):
		self.first = first
		self.middle = middle
		self.last = last
	
	#toString
	def __str__(self):
		return self.first + " " + self.middle + " " + self.last

	def lastFirst(self):
		return self.last + ',' + self.first

	def initials(self):
		return self.first[0] + self.middle[0] + self.last[0]

class Student:
	#fields - name, id, grades(list)
	grades = []
	def __init__(self, name, id):
		self.name = name
		self.id = id

	def addGrade(self, grade):
		self.grades.append(grade)
	
	def showGrades(self):
		grds = ""
		for grade in self.grades:
			grds += str(grade) + " " 
		return grds

	def __str__(self):
		return "Name: "+ self.name + "\n"+\
			"ID: " + self.id + "\n"+\
			"Grades: " + self.showGrades()

	def average(self):
		total = 0
		for grade in self.grades:
			total += grade
		return total/len(self.grades)
		


aName = Name('Mary','Jane','Watson')
print(aName)
print(aName.lastFirst())
print(aName.initials())

stu1 = Student("Jones", '123')
stu1.addGrade(88)
stu1.addGrade(98)
stu1.addGrade(100)
print(stu1)
print("Average: " + str(stu1.average()))
