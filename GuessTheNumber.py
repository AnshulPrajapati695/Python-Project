#---------------------Guess The Number-------------------
import random

#---------------------set a random number----------------
traget=random.randint(1,100)

#---------------------main logic-------------------------
while True:
    Number=input("Guess the Number between 1 to 100 ! OR ouit(Q) : ")

    if(Number=="Q"):
        break
    Number=int(Number)
    if(traget==Number):
        print("Congratulations! you guess the correct number...")
        break

    elif(traget>Number):
        print("Number is too small guess a bigger number...")

    else:
        print("Number is too big guess a smaller number...")


print(".............Game Over!..............")

#-----------------------END OF PROGRAM---------------------
