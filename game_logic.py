import random
from ascii_art import STAGES
from words import WORDS

def get_random_word():
    """Select a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Render current stage, masked word, counters and guessed letters."""
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    display = [ch if ch in guessed_letters else "_" for ch in secret_word]
    print("Word:", " ".join(display))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print(f"Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}\n")

def play_game():
    """Main game loop: prompt until win or mistake limit is reached."""
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win condition: all letters included in guesses
        if all(ch in guessed_letters for ch in secret_word):
            print(f"Congratulations! You saved the Snowman! The word was: {secret_word}")
            break

        # Lose condition: too many mistakes
        if mistakes >= max_mistakes:
            print(f"The Snowman melted! The word was: {secret_word}")
            break

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        # Guess handling
        if guess in secret_word:
            guessed_letters.add(guess)           # correct guess → remember it
            print("Good guess!\n")
        else:
            mistakes += 1                        # wrong guess → increment mistakes
            print("Wrong guess!\n")