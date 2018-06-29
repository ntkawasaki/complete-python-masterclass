# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
print("(Guess 0 to quit game)")
guess = 0  # initialize to number outside of range

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game Over.")
    if guess < answer:
        print("Guess higher.")
    elif guess > answer:
        print("Guess lower.")
    else:
        print("Correct!")