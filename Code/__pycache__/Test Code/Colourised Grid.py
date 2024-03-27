def print_grid(grid, correct_words):
    for row in grid:
        row_correct = any(word in correct_words for word in row)
        if row_correct:
            print_row_in_color(row, '\033[92m')  # Print correct row in green
        else:
            print_row_in_color(row, '\033[91m')  # Print incorrect row in red

    print("Correct words:", correct_words)  # Print the correct words guessed so far

def print_row_in_color(row, color_code):
    print(color_code + "+--------------------+--------------------+--------------------+--------------------+" + '\033[0m')
    for col in row:
        print(color_code + "|{:^20}".format(col), end="")  # Formatting and printing each cell in the grid
    print(color_code + "|" + '\033[0m')
