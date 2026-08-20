"""
Hangman Game

A simple text-based Hangman game.

Key Concepts Used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "hangman", "computer", "keyboard", "elephant"]
MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly pick a word from the list."""
    return random.choice(word_list)


def display_state(word, guessed_letters, incorrect_guesses):
    """Show the word with guessed letters revealed, and blanks for the rest."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord: " + display.strip())
    print("Incorrect guesses left: " + str(MAX_INCORRECT_GUESSES - incorrect_guesses))
    if guessed_letters:
        print("Guessed letters: " + ", ".join(sorted(guessed_letters)))


def get_guess(guessed_letters):
    """Prompt the player for a single, valid, new letter."""
    while True:
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter (a-z).")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
        else:
            return guess


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print("You have " + str(MAX_INCORRECT_GUESSES) + " incorrect guesses allowed.")
    print("=" * 40)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_state(word, guessed_letters, incorrect_guesses)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word: " + word)
            break

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess! '" + guess + "' is in the word.")
        else:
            incorrect_guesses += 1
            print("Sorry, '" + guess + "' is not in the word.")

        # Check loss condition
        if incorrect_guesses == MAX_INCORRECT_GUESSES:
            print("\nGame over! You've run out of guesses.")
            print("The word was: " + word)
            break

    print("\nThanks for playing Hangman!")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Goodbye!")


if __name__ == "__main__":
    main()