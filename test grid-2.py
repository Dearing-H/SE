# def print_grid(grid):
#     for row in grid:
#         print(' | '.join(str(cell) for cell in row))
#         print('-' * (5 * len(row) - 1))

def main():
    # Create a 4x4 grid filled with empty strings
    grid = [[' ' for _ in range(4)] for _ in range(4)]

    print("Welcome to the 4x4 grid!")
    print_grid(grid)

    while True:
        try:
            row = int(input("Enter the row number (0-3): "))
            column = int(input("Enter the column number (0-3): "))
            value = input("Enter the value to populate: ")
            
            if 0 <= row < 4 and 0 <= column < 4:
                grid[row][column] = value
                print("Updated Grid:")
                print_grid(grid)
            else:
                print("Row and Column should be between 0 to 3.")
        except ValueError:
            print("Please enter valid integers for row and column.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

# if __name__ == "__main__":
#     main()
2
# def print_grid(grid):
#     for row in grid:
#         print(' | '.join(str(cell) for cell in row))
#         print('-' * (5 * len(row) - 1))

# def main():
#     # Create a 4x4 grid filled with empty strings
#     grid = [[' ' for _ in range(4)] for _ in range(4)]

#     print("Welcome to the 4x4 grid!")
#     print_grid(grid)

# if __name__ == "__main__":
#     main()

# # Print the current state of the board
# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 5)

# # Get the player's move
# def get_player_move

