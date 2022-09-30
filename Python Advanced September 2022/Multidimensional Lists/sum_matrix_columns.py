rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for row in range(rows):
    line = ([int(x) for x in input().split()])
    matrix.append(line)

for col in range(cols):
    sum_col = 0
    for row in range(rows):
        sum_col += matrix[row][col]
    print(sum_col)

