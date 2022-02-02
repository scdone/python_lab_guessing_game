"""A number-guessing game."""

import random
guess = None
computer_number = random.randint(0, 100)
count = 1


def guessing_game_start():
    name = str(input("Welcome to the Guessing Game. What is your name? "))

    if name:
        global guess
        guess = int(input(f"Let's play, {name}! " "I'm thinking of number between 1 - 100... What's your guess? "))
        guess_again()           
    else:
        print("I can't play if I don't know your name. Goodbye")


def guess_again():
    global guess
    global computer_number
    global count

    if 0 <= guess <= 100 and guess > computer_number and guess % 1 == 0:
        guess = int(input("Your guess is too high. Try again. "))
        count += 1
        guess_again()

    elif 0 <= guess <= 100 and guess < computer_number and guess % 1 == 0:
        guess = int(input("Your guess is too low. Try again. "))
        count += 1
        guess_again()
    
    elif guess == computer_number:
        return print(f"Congrats! You won in {count} guesses.")

    else:
        guess = int(input("Your guess must be a whole number from 0 - 100, inclusive. Try again."))
        guess_again()  


guessing_game_start()
