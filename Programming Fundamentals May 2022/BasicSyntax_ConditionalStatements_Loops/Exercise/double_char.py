command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for char in range(len(command)):
        print(f"{command[char]}" * 2, end='')
    print()

    command = input()
