# Hangman Game

This is a simple text-based Hangman game implemented in Python. The game uses a predefined list of words, and the player has to guess the letters in the word before running out of guesses.

## Features

- Random word selection from a predefined list
- Keeps track of correct and incorrect guesses
- Displays progress after each guess
- Ends the game when the word is guessed or the maximum number of wrong guesses is reached

## Requirements

- Python 3.x

## How to Play

1. Clone the repository or download the `hangman.py` file to your local machine.

2. Open a terminal or command prompt and navigate to the directory where `hangman.py` is located.

3. Run the script using Python:

    ```sh
    python hangman.py
    ```

4. Follow the prompts to guess letters and try to figure out the word before running out of guesses.

## Game Rules

- The game will display a word with underscores representing each unguessed letter.
- Enter one letter at a time to guess a letter in the word.
- If the letter is in the word, all occurrences of the letter will be revealed.
- If the letter is not in the word, it counts as a wrong guess.
- The game continues until you either guess the word correctly or run out of guesses.

## Example Gameplay

