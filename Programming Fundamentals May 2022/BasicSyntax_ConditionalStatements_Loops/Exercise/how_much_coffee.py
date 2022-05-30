command = input()

total_coffees = 0
while command != "END":
    number_of_coffees = 0
    events = ["coding", "dog", "cat", "movie"]
    if command.lower() not in events:
        command = input()
        continue
    else:
        if command.islower():
            number_of_coffees += 1
        elif command.isupper():
            number_of_coffees += 2

    total_coffees += number_of_coffees

    command = input()

if total_coffees > 5:
    print("You need extra sleep")
else:
    print(f"{total_coffees}")
