class Shape:
	def __init__(self, posX, posY):
		self.x = posX
		self.y = posY

	def __str__(self):
		return 'x: '+ str(self.x)+" y: "+str(self.y)+" "
	
	def move(self, x1, y1):
		self.x = self.x +x1
		self.y = self.y +y1

# rectangle inherits shape
class Rectangle(Shape):
	def __init__(self, xcor, ycor, width, height):
		Shape.__init__(self,xcor,ycor)
		self.width = width
		self.height = height

	def __str__(self):
		string = Shape.__str__(self)
		string += "Width: "+str(self.width)+" Height: "+str(self.height)
		return string

rect = Rectangle(5,10,9,8)
print(rect)
rect.move(10,12)
print(rect)