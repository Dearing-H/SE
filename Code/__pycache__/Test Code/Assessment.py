from Categories import *

# for i in esoteric_category["words"]:
#     print(i)

# for i in Technological_category["words"]:
#     print(i)

# for i in Basketball_category["words"]:
#     print(i)

# for i in 
grid = [["Word","Word","Word","Test"],
        ["Word","Word","Word","Word"],
        ["Word","Word","Word","Word"],
        ["Word","Word","Word","Word"]]

categories = [esoteric_category,Technological_category,Basketball_category,Entrances_category,]

row = 0
for category in categories: #for eacch of the connections, access the dictionary
    col = 0
    for word in category["words"]:
        grid[row][col] = word
        col = col + 1 # moves to the coloum
    row = row + 1 # moves to the next row

for row in grid:
    print(row)
