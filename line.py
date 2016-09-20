class Point:
	def __init__(self,x,y):
		self.point = (x,y)

	def __str__(self):
		return "x: "+ str(self.point[0])+" y: " + str(self.point[1])
	
	def setLocation(self,x,y):
		self.point = (x,y)
class Line:
	def __init__(self, p1, p2):
	 	self.p1 = p1
		self.p2 = p2

	def __str__(self):
		return "Point 1: "+ str(self.p1)+"\nPoint 2: "\
			+str(self.p2)

p1 = Point(1,2)
print(p1)
p1.setLocation(10,20)
print(p1)
p2 = Point(8,9)
line1 = Line(p1,p2)
print(line1)
p2.setLocation(12,22)
print(line1)