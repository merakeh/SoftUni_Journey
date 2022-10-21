
turns = input().split(', ')
skip_turn = {player: 0 for player in turns}

matrix = []
for row in range(6):
    line = input().split()
    matrix.append(line)

while True:
    coordinates = input().strip('()').split(', ')
    row, col = [int(x) for x in coordinates]
    if skip_turn[turns[0]]:
        skip_turn[turns[0]] -= 1
        turns[0], turns[1] = turns[1], turns[0]
        continue

    current_symbol = matrix[row][col]
    player = turns[0]     # Takes the first in line/ first form the queue

    if current_symbol == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif current_symbol == "T":
        print(f"{player} is out of the game! The winner is {turns[1]}.")
        break
    elif current_symbol == "W":
        print(f"{player} hits a wall and needs to rest.")
        skip_turn[turns[0]] += 1

    turns[0], turns[1] = turns[1], turns[0]
