class Rational:
	def __init__(self, x,y):
		self.number = x
		if y== 0:
			raise ZeroDivisionError()
		else:
			denom = y
try:
	rat1 = Rational(4,1)
	rat2 = Rational(3,0)
except:
	print("denominator cannot be 0")