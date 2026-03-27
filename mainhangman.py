import hangman_engine as engine
import hangman_visuals as visuals
import os

# Word list moved directly into the file
WORD_LIST = [
    'PYTHON', 'JAVASCRIPT', 'JAVA', 'PROGRAMMING', 'HANGMAN', 
    'DEVELOPER', 'ALGORITHM', 'DATABASE', 'SOFTWARE', 'INTERNET', 
    'COMPUTER', 'NETWORK', 'SECURITY', 'INTERFACE', 'VARIABLE', 
    'FUNCTION', 'MODULE', 'FRAMEWORK', 'LIBRARY', 'SYNTAX'
]

def main():
    """Main game loop for Hangman."""
    visuals.print_welcome()
    
    # Use the local WORD_LIST to pick a secret word
    secret_word = engine.get_word(WORD_LIST)
    
    guessed_letters = []
    tries = 6  # Total tries allowed
    
    print(f"Guess the word! It has {len(secret_word)} letters.")
    print(engine.display_status(secret_word, guessed_letters))
    
    while tries > 0:
        print(visuals.get_hangman_art(tries))
        guess = input("\nEnter a letter guess: ").upper()
        
        # Validate input
        if not engine.is_valid_input(guess, guessed_letters):
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"Correct! '{guess}' is in the secret word.")
        else:
            tries -= 1
            print(f"Oops! '{guess}' is not in the secret word. Tries remaining: {tries}")
        
        status = engine.display_status(secret_word, guessed_letters)
        print(f"\nWord Status: {status}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Check for win condition
        if "_" not in status:
            print("\n" + "="*40)
            print(f"CONGRATULATIONS! YOU WON! The word was {secret_word}.")
            print("="*40)
            break
    else:
        # Check for loss condition
        print(visuals.get_hangman_art(0))
        print("\n" + "="*40)
        print(f"GAME OVER! You ran out of tries. The secret word was {secret_word}.")
        print("="*40)

if __name__ == "__main__":
    main()