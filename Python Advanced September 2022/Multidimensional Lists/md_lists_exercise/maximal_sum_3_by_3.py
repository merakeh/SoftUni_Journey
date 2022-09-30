rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = - 99999999999999
max_sum_matrix = []
for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                      matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2],
                      matrix[row+2][col], matrix[row+2][col +1], matrix[row+2][col+2]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = sub_matrix.copy()

print(f"Sum = {max_sum}")
print(f"{max_sum_matrix[0]} {max_sum_matrix[1]} {max_sum_matrix[2]}")
print(f"{max_sum_matrix[3]} {max_sum_matrix[4]} {max_sum_matrix[5]}")
print(f"{max_sum_matrix[6]} {max_sum_matrix[7]} {max_sum_matrix[8]}")
