import random
from Drugs import *

multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

def chosen_categories():
    game_categories = []
# Generate the game categories

    for index in range(0,4):
        random_index = random.randint(0,len(multiple_categories)-1)
        game_categories.append(multiple_categories[random_index])
        multiple_categories.pop(random_index)

    # Print the chosen categories
    for category in game_categories:
        print(category['words'])

    # Flatten all the words and put them into one big list
    flat_list = []
    for category in game_categories:
        for word in category["words"]:
            flat_list.append(word)

    # Shuffle the words
    random.shuffle(flat_list)
    print(flat_list)

    # Rebuild into grid
    word_index = 0
    row = []
    count = 0
    grid = [flat_list[0:4],flat_list[5:9],flat_list[10:14],flat_list[14:19]]

    for item in grid:
        print(item)

chosen_categories()