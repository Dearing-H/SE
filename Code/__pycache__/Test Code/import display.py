# def create_grid(rows, cols):
#     grid = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             row.append(' ')
#         grid.append(row)
#     return grid

# def add_content_to_grid(grid, content):
#     max_row = max(len(row) for row in content)
#     max_col = len(content)

#     for i, row_content in enumerate(content):
#         for j, cell_content in enumerate(row_content):
#             grid[i][i] = cell_content

#             # If the content is larger than the current grid size, expand the grid
#             if j >= len(grid[i]):
#                 grid[i].extend([' '] * (max_col - len(grid[i])))
#             if i >= len(grid):
#                 grid.append([' '] * max_col)

# # Example usage
# content = [
#     ['A', 'B', 'C'],
#     ['D', 'E'],
#     ['F', 'G', 'H', 'I']
# ]

# grid = create_grid(len(content), len(content[0]))
# add_content_to_grid(grid, content)

# # Display the grid
# for row in grid:
#     print(' '.join(row))