# converting grades to *
for grade in open("grades.txt"):
	print(grade, end = "")
	limit = round(int(grade)/5)
	for i in range(0, limit):
		print("*", end ="")
	print("")