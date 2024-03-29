"""A number-guessing game."""
import random

name = input("Hello player - what's your name?")
number = random.randint(1,100)

guess = 0
tries = 0

print(number)

while number != guess:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess > number:
        print("Guess is too high. Try again.")
    elif guess < number:
        print("Guess is too low. Try again.")
    else:
        break


print(f"Your guess is correct! It took you {tries} attempts.")
