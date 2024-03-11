#Importing random library
import random

#Assigning the global variables
a=0
b=0

min= 1
max= 6

roll_again= input("Start rolling the dices? ")

#Start the game and loop it until user quits
while roll_again=="yes" or roll_again=="y":
    print("Dices are rolling...")
    print("Value of dices are...")
            
    a= random.randint(min, max)
    b= random.randint(min, max)
            
    print(a)
    print("Against")
    print(b)
    
    if a== b:
        print("Draw!")
    elif a>b:
        print("You Win!")
    elif a<b:
        print("You Lose!")
    else:
        input("press Enter to exit.")
                    
    roll_again= input("Roll again?:")


def exitprogram():
    if roll_again== "quit" or roll_again=="q":
        quit


exitprogram()
