import Drugs 

def scale_grid(grid, word):
    scaled_grid = []
  
    # Calculate the scaling factor based on the size of the word
    scaling_factor = len(word)
  
    # Scale the grid horizontally
    for row in grid:
        scaled_row = ''
        for char in row:
            scaled_row += char * scaling_factor
        scaled_grid.append(scaled_row)
  
    # Scale the grid vertically
    scaled_grid *= scaling_factor
  
    # Populate the scaled grid with the word
    word_index = 0
    for i in range(len(scaled_grid)):
        if scaled_grid[i] == ' ':
            scaled_grid[i] = word[word_index % len(word)]
            word_index += 1
  
    return scaled_grid
