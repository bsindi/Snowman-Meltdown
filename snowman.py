import random
from stages import STAGES
from words import WORDS

def display_game_state(mistakes, secret_word, guessed_letters):
    # Always stay within the available STAGES
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    # Build display string for the secret word
    display_word = []
    for letter in secret_word:
        display_word.append(letter if letter in guessed_letters else "_")
    print("Word:", " ".join(display_word))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print(f"Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}\n")

def get_random_word():
    """Select a random word from the list."""
    return random.choice(WORDS)

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win condition: all letters guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the Snowman! The word was:", secret_word)
            break

        # Lose condition: too many mistakes
        if mistakes >= max_mistakes:
            print("The Snowman melted! The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        # Update game state
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Good guess!\n")
        else:
            mistakes += 1
            print("Wrong guess!\n")

if __name__ == "__main__":
    play_game()