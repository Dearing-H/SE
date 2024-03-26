# from Drugs import *

# multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

# def chosen_categories():
#     game_categories = []

#     # Generate the game categories
#     for index in range(0,4):
#         random_index = random.randint(0,len(multiple_categories)-1)
#         game_categories.append(multiple_categories[random_index])
#         multiple_categories.pop(random_index)

#     # Print the chosen categories
#     print("Chosen categories:")
#     for category in game_categories:
#         print(category['words'])

#     # Reset the multiple_categories list
#     multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

#     return game_categories

# # Call the randomiser feature
# chosen_categories()
import random 
from Drugs import *
#define the list of my categories 
multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

#Creating a 4x4 grid with random categories
grid = []
for i in range(4):
    row = []
    for j in range(4):
        random_index = random.randint(0,len(multiple_categories)-1)
        row.append(multiple_categories[random_index])
        multiple_categories.pop(random_index)
    grid.append(row)

#Reset the multiple_categories list
multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

# The function to print the grid
# for row in grid:
#     for category in row:
#         print(category['words'])
#         print()