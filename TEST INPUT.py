from Categories import *

# print(esoteric_category)
# print(Technological_category)
# print(Basketball_category)
# print(Entrances_category)

grid = [["Word","Word","Word","Test"],
        ["Word","Word","Word","Word"],
        ["Word","Word","Word","Word"],
        ["Word","Word","Word","Word"]]

grid[0][0] = "Hello"

# # loop through items using a for loop
# for i in esoteric_category["words"]:
#     print(i)

# a bad way might be to individually fill the grid at the start
# grid[0][0] = esoteric_category["words"][0]
# grid[0][1] = esoteric_category["words"][1]
# grid[0][2] = esoteric_category["words"][2]
# grid[0][3] = esoteric_category["words"][3]

# grid[1][0] = Technological_category["words"][0]
# grid[1][1] = Technological_category["words"][1]
# grid[1][2] = Technological_category["words"][2]
# grid[1][3] = Technological_category["words"][3]


# this could be a bad way, lets think about it
# put all the categories in a list
categories = [esoteric_category,Technological_category,Basketball_category,Entrances_category]

# row = 0
# for category in categories: # first of all loop through all 4 dictionaries i have put in an array
#     col = 0 # set the initial col reference to 0 
#     for word in category["words"]: #after getting a category, start a loop that runs through all 4 words within the dictionary
#         grid[row][col] = word # assign the current word to the grid 
#         col += 1 # incrememnt by 1 # jump to the next cell in the row 
#     row += 1 # after all four words from a category have filled a row, move onto the next 


# print(grid)

#outer loop desgined to loop through rows
row = 0
for category in categories: #for eacch of the connections, access the dictionary
    col = 0
    for word in category["words"]:
        grid[row][col] = word
        col = col + 1 # moves to the coloum
    row = row + 1 # moves to the next row

for row in grid:
    print(row)
# how can you randomise the words in the grid