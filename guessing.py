# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

y = random.randint(1,9)
print(y)

count = 0
guess = 0

while guess != y and guess != "exit":
    guess = input(" Enter a random number between 1- 9:")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < y:
        print("too low!")
    elif guess > y:
        print("too high!")
    else:
        print("You got it! It only took you",count,"tries")

