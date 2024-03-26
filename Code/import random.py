import random

# A list of words for each category
comfy_shoes = ['CROC', 'LOAFER', 'MOCCASIN', 'SLIPPER']
feathers = ['BOA', 'HEADDRESS', 'PILLOW', 'SHUTTLECOCK']
programming_languages = ['BASIC', 'JAVA', 'PYTHON', 'RUBY']
strike = ['COBRA', 'INSPIRATION', 'LIGHTNING', 'UNION']

# A list of categories
categories = ['Comfy Shoes', 'Things Made with Feathers', 'Programming Languages', 'Things That Can Strike']

# A list of words for the game
words = comfy_shoes + feathers + programming_languages + strike

# The number of mistakes allowed
mistakes = 4

# The game loop
while True:
    # Shuffle the words
    random.shuffle(words)

    # Print the words
    print('Wordle for Connections')
    print('----------------------')
    for i in range(8):
        print(f'{i+1}: {words[i]}')

    # Get the user's guess
    guess = input('Enter your guess (one word per category, comma-separated): ').strip().split(',')

    # Check the guess
    if len(guess) != 4:
        print('Please enter exactly one word per category, comma-separated.')
    elif guess[0] not in comfy_shoes or guess[1] not in feathers or guess[2] not in programming_languages or guess[3] not in strike:
        print('That is not a valid guess.')
    else:
        # Remove the correct words
        for i in range(4):
            if guess[i] == words[i]:
                words.pop(i)

        # Print the remaining words
        if len(words) == 0:
            print('Congratulations, you solved the puzzle!')
            break
        elif len(words) < 4:
            print('Nice try, but you have some incorrect guesses.')
            print('Remaining words:')
            for word in words:
                print(word)
        else:
            print('Sorry, those are not the correct words.')
            mistakes -= 1
            if mistakes == 0:
                print('You have run out of mistakes. Better luck next time!')
                break
