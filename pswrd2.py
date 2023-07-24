default = "HERMES"
counter = 3
while True:
	password= input("--ENTER THE PASSWORD--: ")
	if default == password:
		print("--WELCOME USER--")
		break
	else:
		counter-=1
		print(str(counter)+" ATTEMPTS LEFT")
		
		if counter ==0:
			print("--DENIED ALL ACCESS--")
			break
	