
rows, cols = [int(x) for x in input().split(', ')]
matrix = []
sum_all = 0
for row in range(rows):
    line = ([int(x) for x in input().split(', ')])
    matrix.append(line)
    sum_all += sum(line)

print(sum_all)
print(matrix)
