# Updated print_grid function to color the grid based on the guessed category
def print_grid(grid, guessed_words):
    for row in grid:
        row_colors = []  # List to store color codes for each cell in the row
        for col in row:
            if col in guessed_words:  # Check if the word has been guessed
                category_color = next((category['color'] for category in word_categories if col in category['words']))# Get the color code based on the category
                row_colors.append(category_color)
            else:
                row_colors.append('white')  # Default to white if the word hasn't been guessed
        print_row_in_color(row, row_colors)  # Print the row with color codes

# Function to print a row with specified color codes for each cell
def print_row_in_color(row, color_codes):
    print("+--------------------+--------------------+--------------------+--------------------+")
    for col, color_code in zip(row, color_codes):
        print(f"|{'':<20}", end="")
    print("|")
    for col, color_code in zip(row, color_codes):
        print(f"|{col:^20}", end="")
    print("|")
    for col, color_code in zip(row, color_codes):
        print(f"|{'':<20}", end="")
    print("|")
    print("+--------------------+--------------------+--------------------+--------------------+")

# Example usage:
word_categories = [
    {'category_name': "esoteric", 'color': 'yellow', 'words': ['Axiom', 'Enigma', 'Paradox', 'Epiphany']},
    {'category_name': "technological", 'color': 'green', 'words': ['Network', 'Interface', 'Protocol', 'Integration']},
    {'category_name': "basketball", 'color': 'blue', 'words': ['Lebron', 'Tea Gardens', 'Spalding', 'Bird']},
    # Add more categories as needed
]

# Example grid and guessed words
example_grid = [
    ['Axiom', 'Bird', 'Network', 'Tea Gardens'],
    ['Paradox', 'Lebron', 'Interface', 'Spalding'],
    ['Epiphany', 'Enigma', 'Protocol', 'Basketball']
]
example_guessed_words = ['Axiom', 'Bird', 'Lebron', 'Epiphany', 'Basketball']

# Print the colored grid
print_grid(example_grid, example_guessed_words)
