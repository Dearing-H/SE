def print_grid(grid, correct_words):
    for row in grid:
        print("+--------------------+--------------------+--------------------+--------------------+")
        for col in row:
            print("|{:^20}".format(col), end="")  # Formatting and printing each cell in the grid
        print("|")
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("Correct words:", correct_words)  # Print the correct words guessed so far
def print_grid(grid, correct_words):
    for row in grid:
        print("+--------------------+--------------------+--------------------+--------------------+")
        for col in row:
            print("|{:^20}".format(col), end="")  # Formatting and printing each cell in the grid
        print("|")
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("Correct words:", correct_words)  # Print the correct words guessed so far
print 