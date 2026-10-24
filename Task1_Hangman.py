import random

# Words taken from your provided English word list
WORDS = [
    "the", "about", "search", "business", "service",
    "people", "school", "health", "world", "music",
    "product", "system", "project", "computer", "science",
    "education", "government", "student", "college",
    "program", "development", "technology", "network",
    "internet", "design", "language", "story", "family",
    "friend", "country", "history", "travel", "future",
    "learning", "quality", "support", "message",
    "information", "community", "security", "software",
    "application", "example", "question", "problem",
    "picture", "building", "available", "management",
    "resources", "digital", "personal", "customer"
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def play_game():
    secret_word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    attempts = 6

    print("\n=== DATHEON HANGMAN GAME ===")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect attempts.")
    print("Enter 0 to quit.")

    while attempts > 0:
        print(HANGMAN_PICS[6 - attempts])

        display = " ".join(
            letter if letter in guessed else "_"
            for letter in secret_word
        )

        print("Word:", display)
        print("Correct guesses:", sorted(guessed) or "None")
        print("Wrong guesses:", sorted(wrong) or "None")
        print("Attempts left:", attempts)

        if all(letter in guessed for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The word was:", secret_word)
            return

        guess = input("Enter one letter: ").strip().lower()

        if guess == "0":
            print("Game ended. Word:", secret_word)
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed or guess in wrong:
            print("You already guessed that letter.")
            continue

        if guess in secret_word:
            guessed.add(guess)
            print("Correct guess!")
        else:
            wrong.add(guess)
            attempts -= 1
            print("Wrong guess!")

    print(HANGMAN_PICS[6])
    print("\nGame over! The word was:", secret_word)


def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("Thank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()
