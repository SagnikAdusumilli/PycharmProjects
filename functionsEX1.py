#0-240 0%
#241-480 15%
#481+ 28%

def tax(amount):
	if amount <= 240:
		return 0
	elif amount >240 and amount <= 480:
		return amount * .15
	else:
		return amount * .28

def netpay(grosspay):
	return grosspay - tax(grosspay)

print("Enter grosspay")
print("The tax is: "+ str(netpay(int(input()))))