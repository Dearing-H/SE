import random

def choose_word(word_list):
    """Choose a random word from the word list."""
    return random.choice(word_list):

def display_hangman(lives):
    """Display the hangman based on the number of lives left."""
    if lives == 5:
        print("  _______     ")
        print(" |/       |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|________    ")
    elif lives == 4:
        print("  _______     ")
        print(" |/       |    ")
        print(" |       O    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|________    ")
    elif lives == 3:
        print("  _______     ")
        print(" |/       |    ")
        print(" |       O    ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print("_|________    ")
    elif lives == 2:
        print("  _______     ")
        print(" |/       |    ")
        print(" |       O    ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")
        print("_|________    ")
    elif lives == 1:
        print("  _______     ")
        print(" |/       |    ")
        print(" |       O    ")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")
        print("_|________    ")
    else:
        print("  _______     ")
        print(" |/       |    ")
        print(" |       O    ")
        print(" |      /|\   ")
        print(" |      /     ")
        print(" |            ")
        print("_|________    ")

def play_hangman(word, lives):
    """Play a game of Hangman."""
    word_guessed = ["_"] * len(word)
    guessed_letters = []

    while lives > 0 and "_" in word_guessed:
        display_hangman(lives)
        print("Word: ", " ".join(word_guessed))
        print("Guessed letters: ", " ".join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess not in word:
            print("That letter is not in the word.")
            lives -= 1
        else:
            for i, letter in enumerate(word):
                if letter == guess:
                    word_guessed[i] = letter
        guessed_letters.append(guess)

    if "_" not in word_guessed:
        print("Congratulations, you've won!")
    else:
        display_hangman(lives)
        print("Sorry, you've run out of lives. The word was '{}'.".format(word))

if __name__ == "__main__":
    word_list = ["python", "programming", "computer", "science", "algorithm"]
    word = choose_word(word_list)
    lives = 6
    play_hangman(word, lives)