
n = int(input())
matrix = []
for _ in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

primary = []
secondary = []

for row in range(n):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][n - row - 1])

# print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")

# Print the absolute difference between the two diagonals
difference = sum(primary) - sum(secondary)
print(abs(difference))
