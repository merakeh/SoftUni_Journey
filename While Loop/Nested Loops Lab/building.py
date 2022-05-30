floors = int(input())
rooms = int(input())
floor_letter = ""
for f in range(floors, 0, -1):
    for r in range(rooms):
        if f == floors:
            floor_letter = "L"
        elif f % 2 == 0:
            floor_letter = "O"
        else:
            floor_letter = "A"

        print(f"{floor_letter}{f}{r}", end=" ")
    print()
