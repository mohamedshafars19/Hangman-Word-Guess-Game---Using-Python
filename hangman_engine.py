import random

def get_word(words):
    """Pick a random word from the list."""
    return random.choice(words)

def display_status(word, guessed_letters):
    """Returns a string representing the current status of the word (e.g., '_ A _ _')."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += f"{letter} "
        else:
            display += "_ "
    return display.strip()

def is_valid_input(user_input, guessed_letters):
    """Validates the user's input."""
    if len(user_input) != 1 or not user_input.isalpha():
        print("Invalid input! Please enter a single letter.")
        return False
    if user_input.upper() in guessed_letters:
        print(f"You already guessed '{user_input.upper()}'!")
        return False
    return True