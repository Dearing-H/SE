# Harrison Dearing 
# Software Engineering Assessment 1 - Connections 
# v1.0

import random
from categories import *
from time import sleep
import sys

# from Type_Writer_test_one import





print("Start the game, PRESS ENTER")  # Unsure if needed as have two start commands, but it works for now
input()
print("Welcome")
sleep(1)
print('To', end=" ")
sleep(1)

print("""
\u001b[31m  
██████   ██████  ███████ ███████ ███    ██ ███    ██ ███████  ██████ ████████ ██  ██████  ███    ██ ███████ 
██   ██ ██    ██ ██      ██      ████   ██ ████   ██ ██      ██         ██    ██ ██    ██ ████   ██ ██      
██████  ██    ██ ███████ ███████ ██ ██  ██ ██ ██  ██ █████   ██         ██    ██ ██    ██ ██ ██  ██ ███████ 
██   ██ ██    ██      ██      ██ ██  ██ ██ ██  ██ ██ ██      ██         ██    ██ ██    ██ ██  ██ ██      ██ 
██████   ██████  ███████ ███████ ██   ████ ██   ████ ███████  ██████    ██    ██  ██████  ██   ████ ███████ 
\u001b[37m

""")

sleep(1)
print("Welcome to BOSSNNECTIONS, this is an imtation of the fan-favourite New York Times Game Connections.")
sleep(1)
print("To Play, you  will need to connect four items from the same categories.")
sleep(1)
print("The Categories vary in diffucluty, GOOD LUCK AND HAVE FUN. Press Enter To Start!")
input()

sleep(2)


# List of multiple categories from the imported dictionaries
multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category, Shakespeare_category, 
                       Ancient_Military_category, Mythological_Creatures_category, Avant_Garde_Art_Movements, Quantum_Mechanics_Concepts, Literary_Devices, Fast_and_Furious_Locations]

# Function to check user's guess against categories
def check_guess_against_categories(guesses, multiple_categories, lives):
    for category in multiple_categories:
        if set(guesses) == set(category["words"]):  # Checking if the guessed words match the words in the category
            print(f"\033[92mYou got it from {category['category_name']}!\033[0m")
            return True, category, lives  # Returning True for correct guess and the category
    lives -= 1  # Decreasing lives if the guess is incorrect
    print(f"\033[91mSorry, that's incorrect. You have {lives} lives left.\033[0m")
    return False, None, lives  # Returning False for incorrect guess


# Function to get user's guess input
def get_guess():
    guesses = []
    for i in range(4):
        word = input(f"Please Enter word {i + 1}: ")# Getting words from the user and increasing the value of words by 1 so it would say Word 1 please, word 2 please and so on
        guesses.append(word)
    return guesses


# Function to print the game grid
# Function to print the game grid with guessed words and colors







# def print_grid(grid, guessed_words):
#     for row in grid:
#         row_colors = []  # List to store color codes for each cell in the row
#         for col in row:
#             if col in guessed_words:  # Check if the word has been guessed
#                 category_color = next((category['color'] for category in word_categories if col in category['words']), 'white')  # Get the color code based on the category
#                 row_colors.append(category_color)
#             else:
#                 row_colors.append('white')  # Default to white if the word hasn't been guessed
#         print_row_in_color(row, row_colors)  # Print the row with color codes

# # Function to print a row with specified color codes for each cell
# def print_row_in_color(row, color_codes):
#     print("+--------------------+--------------------+--------------------+--------------------+")
#     for col, color_code in zip(row, color_codes):
#         print(f"|{'':<20}", end="")
#     print("|")
#     for col, color_code in zip(row, color_codes):
#         print(f"|{col:^20}", end="")
#     print("|")
#     for col, color_code in zip(row, color_codes):
#         print(f"|{'':<20}", end="")
#     print("|")
#     print("+--------------------+--------------------+--------------------+--------------------+")








def print_grid(grid, correct_words):
    for row in grid:
        row_correct = any(word in correct_words for word in row) #
        if row_correct:
            print_row_in_color(row, '\033[92m')  # Print correct row in green
        else:
            print_row_in_color(row, '\033[91m')  # Print incorrect row in red

    # print("Correct words:", correct_words)  # Print the correct words guessed so far

def print_row_in_color(row, color_code):
    print(color_code + "+--------------------+--------------------+--------------------+--------------------+" + '\033[0m')
    for col in row:
        print(color_code + "|{:^20}".format(col), end="")  # Formatting and printing each cell in the grid
    print(color_code + "|" + '\033[0m')
    print(color_code + "+--------------------+--------------------+--------------------+--------------------+" + '\033[0m')


# Function to convert a flat list into a grid
def convert_flat_list_into_grid(flat_list):
    grid = []
    for i in range(0, len(flat_list), 4):  # Creating rows with 4 elements each
        row = flat_list[i:i+4]  # Slicing the flat list into rows
        grid.append(row + [""] * (4 - len(row)))  # Padding rows with empty strings if needed
    return grid 

# Function to run the game with chosen categories
def chosen_categories():
    game_won = False
    lives = 4  # Initial number of lives
    game_categories = []  # Empty list to store chosen categories
    guessed_correct_count = 0 
    # Randomly select and add categories to the game
    for _ in range(4):
        random_index = random.randint(0, len(multiple_categories) - 1)  # Random index for selecting a category
        game_categories.append(multiple_categories[random_index])  # Add the selected category to the game categories list
        multiple_categories.pop(random_index)  # Remove the selected category from the multiple_categories list to avoid repetition

    flat_list = []  # Empty list to store words from chosen categories
    for category in game_categories:
        for word in category["words"]:
            flat_list.append(word)  # Add words from each category to the flat list

    random.shuffle(flat_list)  # Shuffle the flat list to randomize word positions in the grid
    correct_words = []  # Empty set to store correct words guessed by the user
    print_grid(convert_flat_list_into_grid(flat_list), correct_words)  # Print the initial game grid

    while lives > 0 and game_won == False:  # Loop until lives run out
        guesses = get_guess()  # Get user's guesses
        correct_guess, correct_category, lives = check_guess_against_categories(guesses, game_categories, lives)  # Check if guesses are correct
        # print(f"correct category variable currently is: {correct_category}")
        # print(f"correct words variable currently is: {correct_words}")
        if correct_guess:
            guessed_correct_count  +=1

            correct_words.extend(correct_category["words"])  # Update the set of correct words with words from the correct category
            
            # print(f"correct words variable updated to : {correct_words}")
            flat_list = correct_words + random.sample([word for word in flat_list if word not in correct_words], len(flat_list) - len(correct_words))  # Move correct words to the top and shuffle the rest
            # print(f"flat list currently is: {flat_list}")
            
            if guessed_correct_count == 4:
                game_won = True
            print_grid(convert_flat_list_into_grid(flat_list), correct_words)  # Print the updated game grid


    if game_won == False:
        print("Game over! You ran out of lives.")  # Print game over message when lives run out
    else:
        print("You win at life")
    replay = input("Do you want to play again? (yes/no): ").lower()  # Ask the user if they want to play again
    if replay == "yes":
        chosen_categories()  # Restart the game if the user wants to play again
    else:
        print("Thank you for playing!")

# Run the chosen_categories function to start the game
chosen_categories()



# def shuffle_and_print(lst, correct_set):
#     # (""Shuffles a given list")
#     random.shuffle(lst)
#     print_grid(lst, correct_set)


# issues 
# The grid reshuffles when the categories are guessed correctly
# How to change colours if guessed correctly
# How to make a shuffle button that only shuffles the categories that have not been guessed correctly 
# Make it not case sensitive
# Make the the words not need dashes
# When u get a guess correct correct text is green when wrong text is red 

# if"Shuffle" get_guess
# input from player to shuffle