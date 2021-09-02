import random
import sys

print("Guess the number")
number = random.randint(1, 15)
while True:
    a = input()
    if (int(a) != number):
        print("Nope! Guess again.")
    else:
        print("You guessed it!")
        sys.exit()
        break
