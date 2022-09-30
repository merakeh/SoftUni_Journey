n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()

while command[0] != "END":
    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if row < 0 or row >= n or \
       col < 0 or col >= n:
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value

    command = input().split()

for i in range(n):
    print(*matrix[i], sep=' ')
    