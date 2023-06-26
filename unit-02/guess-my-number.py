#!/usr/bin/env python3

print("Please think of a number between 0 and 100!")

min = 0
max = 100

while True:
    guess = (min + max) // 2
    print("Is your secret number", str(guess) + "?")

    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans != "h" and ans != "l" and ans !="c":
        print("Sorry, I did not understand your input.")
        continue

    if ans == "c":
        print("Game over. Your secret number was:", guess)
        break

    elif ans == "h":
        max = guess

    else:
        min = guess
