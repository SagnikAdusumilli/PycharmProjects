def take(num, list):
	rlist = []
	if num >=0:
		for i in range(0,num):
			rlist.append(list[i])
	else: 
		for i in range(len(list)+num, len(list)):
			rlist.append(list[i])
	return rlist

def drop(num, list):
	rlist = []
	if num>=0:
		for i in range(num, len(list)):
			rlist.append(list[i])
	else:
		for i in range(0, len(list)+num):
			rlist.append(list[i])
	return rlist

	

names = ["Raymond", "Cynthia", "David", "Jennifer", "Clayton"]
someNames = take(-3, names)
print(someNames)
names = drop(-3,names)
print(names)