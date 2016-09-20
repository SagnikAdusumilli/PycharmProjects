#answer = "Watson"
#print("here is a guessing game. You get three tries")
#print("What is the name of the computer that played on Jeopardy?")
#response = raw_input()
#if response == answer:
#	print("you're right! Congratulations!")
#else:
#	print("nope. guess again")
#	response = raw_input()
#	if response == answer:
#		print("you're right!")
#	else:
#		print("wrong. One more guess")
#		response = raw_input()
#		if response == answer:
#			print("correct!")
#		else:
#			print("sorry, you lost!")

# while loop version
tries = 0
awnser = "Watson"
print("what is the name of the computer that played on Jeopardy?")
while(tries < 3):
	response = raw_input()
	if(response == awnser):
		print("Correct!")
		break
	elif tries <3:
		print("wrong!")
		tries = tries +1
		print ( "you have "+ str(3-tries) +" tries left")
	if tries == 3:
		print("you ran out of tries, Game over")
		break
	

		
		