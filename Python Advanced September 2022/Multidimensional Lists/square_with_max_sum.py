
rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)

max_sum = - 99999999999999
max_sum_matrix = []
for row in range(rows - 1):
    for col in range(cols - 1):
        current_square = [matrix[row][col], matrix[row][col + 1],
                          matrix[row + 1][col], matrix[row + 1][col + 1]]

        current_sum = sum(current_square)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = current_square.copy()

print(f"{max_sum_matrix[0]} {max_sum_matrix[1]}")
print(f"{max_sum_matrix[2]} {max_sum_matrix[3]}")
print(max_sum)