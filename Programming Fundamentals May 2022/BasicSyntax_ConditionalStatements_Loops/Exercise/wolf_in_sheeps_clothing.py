sequence = input().split(', ')

for position in range(len(sequence)):

    if sequence[position] == "wolf" and position == len(sequence)-1:
        print("Please go away and stop eating my sheep")
    elif sequence[position] == "wolf":
        print(f"Oi! Sheep number {position}! You are about to be eaten by a wolf!" )

