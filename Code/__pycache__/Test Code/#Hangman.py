#Hangman
#picks word
 #must be alphanumeric A-Z0-9
    #must be == 1 character in length
    #checks if letter is in the word
    #Display the workd w/guessed letters
    #10 guesses


def secret_word():
    #choses a word to use for the game
    word = "Mississippi"
    return word

def get_player_guess():
   
    guess = input ("Please guess a letter")

    while len(guess) != 1 and (guess.isalpha() is False):
        guess = input("Please guess a leter")

    return guess

print(get_player_guess())

