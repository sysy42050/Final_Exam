# Syann Hollins
# 3/7/19
# Dice Roll

# Imported necessary modules

import random

how_many_times = int(input("How many times do you want to roll the dice: "))

min = 1
max = 6


for i in range(how_many_times):
    roll_again = random.randint(1,6)

def user_guess(roll_again):
    while True:
        guess = int(input("Enter value 1 to 6 : "))
        if guess == roll_again:
            print("You got it!")
            break
        print("Try again")
        print("")
user_guess(roll_again)

total = 0

how_many_rolls = int(input("How many rolls do you need to average? "))

print ("")

