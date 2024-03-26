# from Dictionary import *

# for category in game_categories:
#     print( category['words'])

from Drugs import *

multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]


def chosen_categories():
    game_categories = []
# Generate the game categories

    for index in range(0,4):
        random_index = random.randint(0,len(multiple_categories)-1)
        game_categories.append(multiple_categories[random_index])
        multiple_categories.pop(random_index)

    for category in game_categories:
       print( category['words'])

chosen_categories()