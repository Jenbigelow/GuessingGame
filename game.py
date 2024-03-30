"""A number-guessing game."""
import random

def guessing_game():
    name = input("Hello player - what's your name?")
    number = random.randint(1,100)

    guess = 0
    tries = 0


    while number != guess:
        tries += 1
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Guess needs to be between 1 and 100.")
            elif guess > number:
                print("Guess is too high. Try again.")
            elif guess < number:
                print("Guess is too low. Try again.")
            else:
                break
        except:
            print("You did not enter a valid integer between 1 and 100.")


    print(f"Your guess is correct! It took you {tries} attempts.")
    return tries


def play_the_game_again():
    comparing_attempts = []
    while True:
       tries = guessing_game()
       comparing_attempts.append(tries)
       answer = input("Do you want to play again? Y/N  ").lower()
       if answer == "n":
            break
       

    print(min(comparing_attempts))
    return min(comparing_attempts)



play_the_game_again()



         