print("-------------------------------------------------------")
print("--THE COMPUTER WILL DETECT THE PLACEMENT OF THE NUMBERS--")
print("-------------------------------------------------------")
num1 = int(input("--ENTER NUMBER 1--: "))
num2 = input("--ENTER NUMBER 2--: ")
num3 = input("--ENTER NUMBER 3--: ")
print("-------------------------------------------------------")
if num1 > num2 and num1 > num3:
    print("--"+num1+" IS GREATER--")
    if num2 > num3:
            print("--"+num2+" IS THE MEDIAN--")
            print("--"+num3+" IS LESSER--")
    else:
            print("--"+num3+" IS THE MEDIAN--")
            print("--"+num2+" IS LESSER--")
if num2 > num1 and num2 > num3:
    print("--"+num2+" IS GREATER--")
    if num3 > num1:
            print("--"+num3+" IS THE MEDIAN--")
            print("--"+num1+" IS LESSER--")
    else:
            print("--"+num1+" IS THE MEDIAN--")
            print("--"+num3+" IS LESSER--")
if num3 > num2 and num3 > num1:
    print("--"+num3+" IS GREATER--")
    if num2 > num1:
            print("--"+num2+" IS THE MEDIAN--")
            print("--"+num1+" IS LESSER--")
    else:
            print("--"+num1+" IS THE MEDIAN--")
            print("--"+num2+" IS LESSER--")            
print("-------------------------------------------------------")