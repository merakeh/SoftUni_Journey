
n = int(input())

matrix = []
for row in range(n):
    line = list(input())
    matrix.append(line)

searched_symbol = input()
found = False

for row in range(n):
    for col in range(n):
        if searched_symbol == matrix[row][col]:
            print(f"({row}, {col})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{searched_symbol} does not occur in the matrix")