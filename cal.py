print(" ")
print("CALCULATOR")
print(" ")
print("---------------------------------------------------------------------------------------------------------------------")
print(" ")

num1 = float(input("ENTER THE FIRST NUMBER:"))

print(" ")
print("---------------------------------------------------------------------------------------------------------------------")
print(" ")

operator = input("ENTER AN OPERATOR (+, -, *, /):")

print(" ")
print("---------------------------------------------------------------------------------------------------------------------")
print(" ")

num2 = float(input("ENTER THE SECOND NUMBER:"))

print(" ")
print("---------------------------------------------------------------------------------------------------------------------")
print(" ")

if operator == "+":
	print(num1+num2)
elif operator == "-":
	print(num1-num2)
elif operator == "*":
	print(num1*num2)
elif operator == "/":
	if(num2==0):
		print("CANT DIVIDE BY 0")
	else:
		print(num1/num2)
else:
	print("INVALID OPERATOR. PLEASE TRY AGAIN.")

print(" ")
print("---------------------------------------------------------------------------------------------------------------------")