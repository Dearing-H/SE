from  Drugs import *
import random
import curses

# Define the list of categories
multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

# Define the grid size
GRID_SIZE = 4

# Define the colors
colors = [curses.color_pair(i) for i in range(1, 8)]

def chosen_categories():
    game_categories = []
# Generate the game categories

    for index in range(0, GRID_SIZE):
        random_index = random.randint(0, len(multiple_categories) - 1)
        game_categories.append(multiple_categories[random_index])
        multiple_categories.pop(random_index)

    # Flatten all the words and put them into one big list
    flat_list = []
    for category in game_categories:
        for word in category["words"]:
            flat_list.append(word)

    # Shuffle the words
    random.shuffle(flat_list)

    # Rebuild into grid
    grid = [flat_list[0:GRID_SIZE], flat_list[GRID_SIZE:2*GRID_SIZE], flat_list[2*GRID_SIZE:3*GRID_SIZE], flat_list[3*GRID_SIZE:]]

    return grid, flat_list

def print_grid(grid, flat_list, colors):
    # Clear the screen
    stdscr.clear()

    # Print the grid
    for i, row in enumerate(grid):
        for j, word in enumerate(row):
            # Set the color for the word
            curses.attron(colors[i % len(colors)])
            curses.addstr(i, j * 3, word)
            curses.attroff(curses.color_pair(i % len(colors)))

    # Print the flat list
    for i, word in enumerate(flat_list):
        # Set the color for the word
        curses.attron(colors[i % len(colors)])
        curses.addstr(GRID_SIZE + i // GRID_SIZE, (i % GRID_SIZE) * 3, word)
        curses.attroff(curses.color_pair(i % len(colors)))

    # Refresh the screen
    curses.doupdate()

def main():
    # Initialize curses
    curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.curs_set(False)

    # Set up the colors
    for i in range(1, 8):
        curses.init_pair(i, i, curses.COLOR_BLACK)

    # Choose the categories
    grid, flat_list = chosen_categories()

    # Main loop
    while True:
        # Print the grid and flat list
        print_grid(grid, flat_list, colors)

        # Wait for user input
        key = curses.getkey()

        # Check for a quit key
        if key in ['q', 'Q']:
            break

        # Check for a space key
        elif key == ' ':
            # Get the user's guess
            guess = input("Enter your guess: ").strip().lower()

            # Check if the guess is in the flat list
            if guess in flat_list:
                # Find the index of the guess in the flat list
                index = flat_list.index(guess)

                # Replace the guess with a larger word
                grid[index // GRID_SIZE][index % GRID_SIZE] = "X"

                # Clear the screen
                curses.clear()

                # Print the grid and flat list
                print_grid(grid, flat_list, colors)

if __name__ == '__main__':
    main()