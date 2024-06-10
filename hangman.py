import random

# Predefined list of words
WORDS = ["python", "django", "hangman", "developer", "openai"]

def get_random_word():
    """Select a random word from the predefined list."""
    return random.choice(WORDS)

def display_word_progress(word, guesses):
    """Return the word display with guessed letters and underscores."""
    return ''.join([letter if letter in guesses else '_' for letter in word])

def play_hangman():
    """Main function to play Hangman."""
    word = get_random_word()
    guesses = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    
    while wrong_guesses < max_wrong_guesses:
        display_word = display_word_progress(word, guesses)
        print(f"\nWord: {display_word}")
        print(f"Guesses: {', '.join(guesses)}")
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")

        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess not in guesses:
                guesses.append(guess)
                if guess not in word:
                    wrong_guesses += 1
                    print(f"Wrong guess! The letter '{guess}' is not in the word.")
                else:
                    print(f"Good guess! The letter '{guess}' is in the word.")
            else:
                print("You've already guessed that letter.")
        else:
            print("Invalid input. Please enter a single letter.")

        if set(word).issubset(set(guesses)):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
