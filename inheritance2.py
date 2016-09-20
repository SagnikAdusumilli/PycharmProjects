class Employee:
	def __init__(self, name, payRate):
		self.name = name
		self.payRate = payRate

	def __str__(self):
		return self.name +", "+ str(self.payRate)
	
	def pay(self, hoursWorked):
		return self.payRate * hoursWorked

class Manager (Employee):
	def __init__(self, name, payRate, isSalaried):
		Employee.__init__(self, name, payRate)
		self.salaried = isSalaried

	def __str__(self):
		return Employee.__str__(self)+\
			" salaried: " + str(self.salaried)

	def pay(self,hoursWorked):
		if self.salaried:
			return self.payRate
		else:
			return hoursWorked*self.payRate

e1 = Employee("Bruce Wane", 11.25)
print(e1)
print("gross pay: "+str(e1.pay(40)))

m1 = Manager("Jane Smith", 1200, True)
print(m1)
print("gross pay: "+str(m1.pay(40)))

m2 = Manager("Nathan Drake", 20.00, False)
print(m2)
print("gross pay: "+str(m2.pay(40)))