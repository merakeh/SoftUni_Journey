
n = int(input())
matrix = []
sum_diagonal = 0
for row in range(n):
    matrix.append([int(x) for x in input().split()])
    sum_diagonal += matrix[row][row]
print(sum_diagonal)
