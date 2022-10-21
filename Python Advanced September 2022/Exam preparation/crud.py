
def get_row_col(row, column, direction):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }
    r = row + directions[direction][0]
    c = column + directions[direction][1]
    return r, c


size = 6
matrix = []

# Create the board\matrix
for _ in range(size):
    matrix.append(input().split())

# Get the initial position and unpack in variables row, col
row, col = [int(i) for i in input().strip('()').split(', ')]

while True:
    command = input()
    if command == "Stop":
        break

    if "Create" in command:
        action, direction, value = command.split(', ')
        row, col = get_row_col(row, col, direction)

        if matrix[row][col] == '.':
            matrix[row][col] = value

    elif "Update" in command:
        action, direction, value = command.split(', ')
        row, col = get_row_col(row, col, direction)

        if matrix[row][col] != '.':
            matrix[row][col] = value

    elif "Delete" in command:
        direction = command.split(', ')[1]
        row, col = get_row_col(row, col, direction)

        if matrix[row][col] != '.':
            matrix[row][col] = '.'

    elif "Read" in command:
        direction = command.split(', ')[1]
        row, col = get_row_col(row, col, direction)

        if matrix[row][col] != '.':
            print(f"{matrix[row][col]}")

for row in matrix:
    print(*row)
