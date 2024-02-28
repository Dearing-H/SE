def generate_secret_word():
    word = "Mississipi"
    return word


def get_player_guess():
    guess = input("Please Guess a letter:")
    while len(guess) != 1 or guess.isdigit():
        guess = input("Please guess a single letter: ")
    print(f"Accepted your letter: {guess}")
    return guess


def display_word_to_guess(secret_word, guesses):
    displayed_word = ""
    for letter in secret_word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word
    

def check_if_won(secret_word,guesses):
    for letter in secret_word:
        if letter not in guesses:
            return False
    return True


def main():
    secret_word = generate_secret_word()
    guesses = []
    attempts = 10

    while attempts > 0 and not check_if_won(secret_word, guesses):
        print(display_word_to_guess(secret_word, guesses))
        guess = get_player_guess()
        if guess not in secret_word:
            attempts -= 1
        guesses.append(guess)
        print(f"Attempts remaining: {attempts}")
    
    if check_if_won(secret_word, guesses):
        print("Congratulations, you won!")
    else:
        print("Out of attempts, you Lost! The word was:", secret_word)

main()
