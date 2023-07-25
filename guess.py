name = input("--ENTER YOUR NAME--: ")
counter = 1
import random
number = random.randint(1, 100)
while True:
    guess = int(input("--ENTER A NUMERIC GUESS BETWEEN 1 AND 100--: "))
    if guess < number:
        print("--HIGHER THAN "+str(guess)+"--")
        counter+=1
    elif guess > number:
        print("--LOWER THAN "+str(guess)+"--")
        counter+=1
    elif guess == number:
        print("--CORRECT--")
        print("--CONGRATULATIONS "+name+"--")
        print("--YOU ONLY NEEDED "+str(counter)+" TRY'S--")
        break