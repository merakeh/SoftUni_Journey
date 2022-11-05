
def print_row(size, row):
    print((size - row) * ' ', end='')
    print('* ' * row)


n = int(input())

for r in range(1, n + 1):
    print_row(n, r)

for r in range(n - 1, -1, -1):
    print_row(n, r)
