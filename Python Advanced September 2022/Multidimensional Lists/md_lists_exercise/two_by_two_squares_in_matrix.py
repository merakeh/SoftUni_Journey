
rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

counter_squares = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        a = matrix[row][col]
        b = matrix[row][col + 1]
        c = matrix[row + 1][col]
        d = matrix[row + 1][col + 1]

        if a == b == c == d:
            counter_squares += 1

print(counter_squares)