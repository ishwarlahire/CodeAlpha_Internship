# TASK 1: Hangman Game Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time. Simplified Scope: ● Use a small list of 5 predefined words (no need to use a file or API). ● Limit incorrect guesses to 6. ● Basic console input/output — no graphics or audio. Key Concepts Used: random, while loop, if-else, strings, lists.
import random

words = ["python", "apple", "mango", "chair", "tiger"]

word = random.choice(words)
guessed = []
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("You Win!")
        break

    guess = input("Enter letter: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        chances -= 1
        print("Wrong Guess! Chances left:", chances)

if chances == 0:
    print("You Lose! Word was:", word)