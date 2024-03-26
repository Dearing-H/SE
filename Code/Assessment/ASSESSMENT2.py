# from Dictionary import *

# for category in game_categories:
#     print( category['words'])
import random
from Drugs import *

multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

def check_guess_against_the_original_dictionaries(guesses, multiple_categories):
    print(guesses)
    # print(multiple_categories)
    # can i compare my guesses list to all of the word lists inside each categories
    for category in multiple_categories:
        print(category["words"])
        if set(guesses) == set(category["words"]):
            print("You got it pal")


def get_guess():
    # word_one = input("word please:")
    # word_two = input("word please: ")
    # word_three = input("word please")
    # word_four = input("word please")
    your_guesses = input("Type words followed by commas")
    guesses = your_guesses.split(",")
        # guesses = [word_one, word_two, word_three, word_four]

    
    return guesses

def take_horizontal_grid_and_display_correctly(grid):
    for row in grid:
        print(row)

def convert_flat_list_into_grid(flat_list):
    grid = []
    row = [flat_list[0], flat_list[1], flat_list[2], flat_list[3]]
    row_two = [flat_list[4], flat_list[5], flat_list[6], flat_list[7]]
    row_three = [flat_list[8], flat_list[9], flat_list[10], flat_list[11]]
    row_four = [flat_list[12], flat_list[13], flat_list[14], flat_list[15]]
    grid.append(row)
    grid.append(row_two)
    grid.append(row_three)
    grid.append(row_four)
    return grid 

def chosen_categories():
    game_categories = []
# Generate the game categories

    for index in range(0,4):
        random_index = random.randint(0,len(multiple_categories)-1)
        game_categories.append(multiple_categories[random_index])
        multiple_categories.pop(random_index)

    # #print the categories
    # for category in game_categories:
    #     print(category['words'])

    # flatten all the words and put them into one big list
    # shuffle the words
    # rebuild into grid
    flat_list = []
    for category in game_categories:
        for word in category["words"]:
            flat_list.append(word)

    random.shuffle(flat_list)
    # print(flat_list)
    grid = convert_flat_list_into_grid(flat_list) # run fongs new function to put flat list into the grid
    take_horizontal_grid_and_display_correctly(grid)


    guesses = get_guess()
    check_guess_against_the_original_dictionaries(guesses,multiple_categories)

    # word_index = 0
    # row = []
    # count = 0
    
    # grid = [flat_list[0:4],flat_list[5:9],flat_list[10:14],flat_list[14:19]]

    # for item in grid:
    #     print(item)



chosen_categories()


