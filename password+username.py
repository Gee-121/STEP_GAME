name = "HERMES"
default = "BYTE4644"
counter = 3
while True:
	username = input("--ENTER USERNAME--:")
	password= input("--ENTER THE PASSWORD--: ")
	if username == name and password == default:
		print("--WELCOME HERMES--")
		break
	else:
		counter-=1
		print(str(counter)+" ATTEMPTS LEFT")
		if counter ==0:
			print("--DENIED ALL ACCESS--")
			break
	