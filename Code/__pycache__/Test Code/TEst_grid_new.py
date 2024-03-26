grid_size = 5  # number of rows/columns in the grid

# Create a grid using triple-quoted strings
grid = (
    f"|{' ' * (grid_size * 11)}|" f"\n"
    f"|{'-' * (grid_size * 11)}|" f"\n"
) * grid_size

# Fill the grid with the desired content
content = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "Y"],
]

for row in range(grid_size):
    for col in range(grid_size):
        # Insert the content at the correct position
        grid = grid[: (row * (grid_size + 1) + col * 11 + 2)] + (
            f"| {content[row][col]} " * (grid_size + 1)
        )
    grid += "|\n"
grid += "+" + "-" * (grid_size * 11) + "+"

print(grid)