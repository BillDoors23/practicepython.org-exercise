"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.

Extra:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

rand_num = random.randint(1, 9)
guess_num = 0
count_guess = 0

while guess_num != rand_num and guess_num != 'exit':
    try:

        guess_num = input("Enter your guess number: ")

        if guess_num == 'exit':
            break

        guess_num = int(guess_num)
        count_guess += 1

        if guess_num > rand_num:
            print("lower")
            continue
        if guess_num < rand_num:
            print("higher")
        if guess_num == rand_num:
            print("CORRECT")
            
    except ValueError:
        print("invalid input!")
        continue

print("%s tries!" % count_guess)
