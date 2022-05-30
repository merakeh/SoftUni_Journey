command = input()

while command != "Welcome!":
    house = ''
    if command == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(command) < 5:
        house = "Gryffindor"
    elif len(command) == 5:
        house = "Slytherin"
    elif len(command) == 6:
        house = "Ravenclaw"
    elif len(command) > 6:
        house = "Hufflepuff"

    print(f"{command} goes to {house}.")
    command = input()
else:
    print("Welcome to Hogwarts.")
