# 2 D Arrays

grid = []
placeholder = 1

for row in range (0,4):
    row = []
    for col in range(0,4):
        row.append(placeholder)
        placeholder += 1
    grid.append(row)

print(grid[0]) # refers to the entire first row
print(grid[0][0]) # refers to a specific cell

for row in grid:
    print(row)
