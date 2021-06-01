# Importing random module...
import random

# Title
print("\t \t Number Guessing Game")

# Getting input Name
Name = input("Enter Your Name: ")
# game introduction...
print("Welcome {0}!...i am peter i choose one random number in between 1 to 40, Can you guess that number!!".format(Name))

# picking a random number from in between 1 to 40...
random_number = random.randint(1,40)

# looping count start
count = 1
# limitation of game
limit = 5
# input
Guess = int(input("{0}. Guess the number: ".format(count)))

while Guess != random_number: # if the condition is false than the last print-statement execute.
    while count < limit:
        count += 1  #Increment

        # if else statement for True execution...
        if Guess > random_number:
            Guess = int(input("{0}. Sorry, Guess lesser than {1}: ".format(count,Guess)))
        else:
            Guess = int(input("{0}. Sorry, Guess higher than {1}: ".format(count,Guess)))

        # For warning message...
        if count == 4:
            print("\t Last chance")

        # limitation reached...
        if count == limit:
            while random_number != Guess:
                 print("You loss, the number is " + str(random_number) + " Better luck next time!")
                 break
        break

print("You Win congrats! ",Name)

