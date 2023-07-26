import random 
ROCK = 1
PAPER = 2
SCISSORS = 3
GUN = 4
lose = 0
win = 0
round = 1
print(" ")
print("--ROCK, PAPER, SCISSORS WITH COMPUTER--")
print(" ")
print("--TYPE 1 FOR ROCK--")
print("--TYPE 2 FOR PAPER--")
print("--TYPE 3 FOR SCISSORS--")
print(" ")
while True:
    round+1
    print("--ROUND "+str(round)+"--")
    cpchoice = random.randint(1, 3)
    playoption = int(input("--ROCK, PAPER, OR SCISSORS--: "))
    print("--COMPUTER CHOSE "+str(cpchoice)+"--")
    if (cpchoice == 1 and playoption == 3) or (cpchoice == 3 and playoption == 2) or (cpchoice == 2 and playoption == 1): 
        print("--LOSE--")
        print(" ")
        lose+=1
        round+=1
    if (cpchoice == 3 and playoption == 1) or (cpchoice == 2 and playoption == 3) or (cpchoice == 1 and playoption == 2):
        print("--YOU WIN--")
        print(" ")
        win+=1
        round+=1
    if cpchoice == playoption:
        print("--DRAW--")
        print(" ")
        round+=1
    if playoption == 4:
        print(" ")
        print("--YOU KILLED THE OPONENT--")
        print("--GOOD GAME, YOU WIN--")
        print("--THE AUTHORITIES ARE ON THEIR WAY--")
        break
    if lose ==3:
        print("--YOU LOST, GAME OVER--")
        break
    if win ==3:
        print("--GOOD GAME, YOU WIN--")
        break 



