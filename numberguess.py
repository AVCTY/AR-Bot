import random

#Asking input from user for a number range
num_range= int(input("Enter a number for a guessing range: "))

#Checks that user input integer is a positive number
while num_range<=0:
    print("Enter only a positive integer")
    num_range= int(input("Enter a number for a guessing range: "))
    
number = random.randint(1, num_range)

guess =int(input("Enter your guess: "))

count= 1

#Output for user's guess
while guess != number:
    if guess < number:
        print("Number was too low, try again")
        count+=1
        guess = int(input("Try again. Enter another number: "))
    elif guess > number:
        print("Your number was too high...")
        count+=1
        guess = int(input("Try again. Enter another number: "))
    
    if guess==0 or guess<0:
        print("Sorry you\'ve given up")
        break
    
if guess==number:
        print("Congratulations! You guessed it right! The number I was thinking of was",\
              number,"You tried", count, "time(s)")
