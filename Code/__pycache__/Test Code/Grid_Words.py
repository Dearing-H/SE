words = ["Word 1", "Word 2", "Word 3", "Word 4", "Word 5",
         "Word 6", "Word 7", "Word 8", "Word 9", "Word 10",
          "Word 11", "Word 12", "Word 13", "Word 14", "Word 15",
           "Word 16"]

grid = []
word_index = 0

for row in range(0, 4):
    row = [] # start an empty array
    for col in range(0, 4):
        row.append(words[word_index])
        word_index += 1
    grid.append(row) # add the row to the grid

print(grid)

# import random

# print(random.randint(0, len(words)))