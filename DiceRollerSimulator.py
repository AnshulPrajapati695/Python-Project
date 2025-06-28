#----------------------------Dice Roller Simulator----------------------------
import random

print("Welcome to Dice Roller Simulator!")

#--------------------------------main logic------------------------------------
while True:
    user_input=input("**********Press ENTER to roll OR Q for quit***********")
    if user_input=="Q" or user_input=="q":
        print("-----------Thanks for play the game! Goodbye-----------")
        break
    
    dice=random.randint(1,6)
    print(f"you rolled a {dice}!")

#-------------------------------END OF PROGRAM---------------------------------