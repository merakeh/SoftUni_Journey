
size = int(input())
tracked_car = input()
matrix = []

kilometers = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

car_pos = [0, 0]
tunnels = []

for row in range(size):
    line = input().split()
    matrix.append(line)
    if "T" in line:
        tunnels.append([row, line.index('T')])


while True:
    command = input()

    if command == "End":
        matrix[car_pos[0]][car_pos[1]] = "C"
        print(f"Racing car {tracked_car} DNF.")

        break

    car_pos[0] += directions[command][0]
    car_pos[1] += directions[command][1]

    if matrix[car_pos[0]][car_pos[1]] == '.':
        kilometers += 10
    elif matrix[car_pos[0]][car_pos[1]] == "T":
        matrix[tunnels[0][0]][tunnels[0][1]] = '.'
        matrix[tunnels[1][0]][tunnels[1][1]] = '.'

        if car_pos[0] == tunnels[0][0] and car_pos[1] == tunnels[0][1]:
            car_pos = [tunnels[1][0], tunnels[1][1]]
        else:
            car_pos = [tunnels[0][0], tunnels[0][1]]
        kilometers += 30
    elif matrix[car_pos[0]][car_pos[1]] == 'F':
        matrix[car_pos[0]][car_pos[1]] = "C"
        kilometers += 10
        print(f"Racing car {tracked_car} finished the stage!")
        break


print(f"Distance covered {kilometers} km.")

for row in matrix:
    print(*row, sep='')


