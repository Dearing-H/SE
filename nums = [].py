# nums = []
# for i in range(3):
#     nums.append([])
#     for j in range(1, 4):
#         nums[i].append(j)
# print("3X3 grid with numbers:")
# print(nums) 

# def grid_maker(h,w):
#     grid = [[["-"] for i in range(w)] for i in range(h)]
#     grid[0][0] = ["o"]
#     printgrid

# >>>grid_maker(3,5) => [[['o'], ['-'], ['-'], ['-'], ['-']], [['-'], ['-'], ['-'], ['-'], ['-']], [['-'], ['-'], ['-'], ['-'], ['-']]]

def print_grid(rows, cols):
    for i in range(rows):
        # Print the top border of the grid
        print("+" + "---+" * cols)

        # Print the content of the grid
        print("|" + "   |" * cols)

    # Print the bottom border of the grid
    print("+" + "--+" * cols)

# Define the dimensions of the grid
rows = 4
cols = 4

# Call the function to print the grid
print_grid(rows, cols)


