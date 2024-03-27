# Harrison Dearing 
# Software Engineering Assessment 1 - Connections 
# v1.0

import random
from categories import *


# List of multiple categories from the imported dictionaries
multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category, Shakespeare_category, 
                       Ancient_Military_category, Mythological_Creatures_category, Avant_Garde_Art_Movements, Quantum_Mechanics_Concepts, Literary_Devices, Fast_and_Furious_Locations]

# Function to check user's guess against categories
def check_guess_against_Categories(guesses, multiple_categories, lives):
    for category in multiple_categories:
        if set(guesses) == set(category["words"]):  # Checking if the guessed words match the words in the category
            print("You got it!")
            return True, category  # Returning True for correct guess and the category
    lives -= 1  # Decreasing lives if the guess is incorrect
    print(f"Sorry, that's incorrect. You have {lives} lives left.")
    return False, None  # Returning False for incorrect guess and no category

# Function to get user's guess input
def get_guess():
    your_guesses = input("Type words separated by spaces: ")
    guesses = your_guesses.split(" ")  # Splitting user input into a list of words
    return guesses

# Function to print the game grid
def print_grid(grid, correct_words):
    for row in grid:
        print("+--------------------+--------------------+--------------------+--------------------+")
        for col in row:
            print("|{:^20}".format(col), end="")  # Formatting and printing each cell in the grid
        print("|")
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("Correct words:", correct_words)  # Print the correct words guessed so far

# Function to convert a flat list into a grid
def convert_flat_list_into_grid(flat_list):
    grid = []
    for i in range(0, len(flat_list), 4):  # Creating rows with 4 elements each
        row = flat_list[i:i+4]  # Slicing the flat list into rows
        grid.append(row + [""] * (4 - len(row)))  # Padding rows with empty strings if needed
    return grid 

# Function to run the game with chosen categories
def chosen_categories():
    lives = 4  # Initial number of lives
    game_categories = []  # Empty list to store chosen categories
    
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
    correct_words = set()  # Empty set to store correct words guessed by the user
    print_grid(convert_flat_list_into_grid(flat_list), correct_words)  # Print the initial game grid

    while lives > 0:  # Loop until lives run out
        guesses = get_guess()  # Get user's guesses
        correct_guess, correct_category = check_guess_against_Categories(guesses, game_categories, lives)  # Check if guesses are correct
        if correct_guess:
            correct_words.update(set(correct_category["words"]))  # Update the set of correct words with words from the correct category
            flat_list = list(correct_words) + random.sample([word for word in flat_list if word not in correct_words], len(flat_list) - len(correct_words))  # Move correct words to the top and shuffle the rest
            print_grid(convert_flat_list_into_grid(flat_list), correct_words)  # Print the updated game grid
        lives -= 1  # Decrement lives after each guess

    print("Game over! You ran out of lives.")  # Print game over message when lives run out

    replay = input("Do you want to play again? (yes/no): ").lower()  # Ask the user if they want to play again
    if replay == "yes":
        chosen_categories()  # Restart the game if the user wants to play again
    else:
        print("Thank you for playing!")

# Run the chosen_categories function to start the game
chosen_categories()