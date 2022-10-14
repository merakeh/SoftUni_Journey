
def eat_cookies(presents_left, kids_visited):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == 'V':
                kids_visited += 1

            neighborhood[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, kids_visited


count_of_presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []

count_nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    neighborhood.append(line)

    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighborhood[row][santa_pos[1]] = '-'

    count_nice_kids += line.count('V')

command = input()


while True:
    if command == "Christmas morning":
        break

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        nice_kids_visited += 1
        count_of_presents -= 1
    elif house == 'C':
        count_of_presents, nice_kids_visited = eat_cookies(count_of_presents, nice_kids_visited)

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    if not count_of_presents or nice_kids_visited == count_nice_kids:
        break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = "S"

if not count_of_presents and nice_kids_visited < count_nice_kids:
    print("Santa ran out of presents!")

print(*[' '.join(row) for row in neighborhood], sep='\n')

if nice_kids_visited == count_nice_kids:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_kids - nice_kids_visited} nice kid/s.")