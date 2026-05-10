import random

def play_hangman():
    # 1. Setup: Predefined word list
    words = ["python", "jupiter", "keyboard", "coding", "pixel"]
    secret_word = random.choice(words)
    
    # 2. State tracking
    guessed_letters = []
    attempts_remaining = 6
    
    print("--- Welcome to Hangman! ---")
    print(f"The word has {len(secret_word)} letters.")

    # 3. Main Game Loop
    while attempts_remaining > 0:
        # Display the current progress (e.g., "p _ t h _ n")
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Check for win condition
        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break

        # 4. Input and Logic
        guess = input("Guess a letter: ").lower()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        # 5. Check if guess is correct
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_remaining -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    # 6. Game Over
    if attempts_remaining == 0:
        print("\nGame Over!")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
