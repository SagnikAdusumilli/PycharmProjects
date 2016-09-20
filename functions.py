def square(number):
	return number*number

def isVowel(l):
	if l == 'a' or l == 'e' or l == 'i' or l == 'o'\
	   or l == 'u':
		return True
	else:
		return False
	

def numVowels(string):
	string = string.lower()
	count = 0
	for l in string:
		if isVowel(l):
			count += 1
	return count

print("Enter a number")
num = square(int(input()))
print("the square is: "+ str(num))
print("Enter a word")
string = input()
print("the number of vowels: "+ str(numVowels(string)))

