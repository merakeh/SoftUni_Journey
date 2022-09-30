
# create a dictionary with the directions' indexes
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = int(input())
matrix = []
bunny_pos = []
best_path = []
max_collected_eggs = 0
best_direction = None

# read the matrix from input
for row in range(size):
    line = input().split()

    # Check if the bunny 'B' is in the line
    if "B" in line:
        bunny_pos = [row, line.index('B')]    # take B's index as the column value

    matrix.append(line)


# Unpack the directions dictionary to use as guide of movement
for direction, positions in directions.items():    # positions is a tuple of indexes
    row, col = [    # We set 'row' and 'col' to use them as current position of the bunny
        bunny_pos[0] + positions[0],    # "moving" the B across the matrix's rows
        bunny_pos[1] + positions[1]     # "moving" the B across the matrix's columns
    ]

    # For each movement we set the path and collected eggs to zero
    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:    # while the indexes are valid
        # Check whether we have reached a trap
        if matrix[row][col] == "X":
            break

        # If we have not been trapped, we collect eggs and save our path
        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        # We then move to the next position without collecting anything
        # Just to be ready for the next iteration
        row += positions[0]
        col += positions[1]

        # Searching for the maximum eggs collected and the best direction
        if collected_eggs >= max_collected_eggs:
            max_collected_eggs = collected_eggs
            best_direction = direction
            best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)
