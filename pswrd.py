default = "HERMES"
counter = 0
while True:
	password= input("--ENTER THE PASSWORD--: ")
	if default == password:
		print("--WELCOME USER--")
		break
	else:
		print("--ACCESS DENIED, TRY AGAIN.--")
		counter+=1
		if counter ==3:
			print("--DENIED ALL ACCESS--")
			break
	