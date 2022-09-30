number_of_wagons = int(input())
train = [0] * number_of_wagons
command = input()

while command != "End":

    data = command.split(" ")
    current_command = data[0]

    if current_command == "add":
        people_to_add = int(data[1])
        train[-1] += people_to_add
    elif current_command == "insert":
        index = int(data[1])
        people_to_insert = int(data[2])
        train[index] += people_to_insert
    elif current_command == "leave":
        index = int(data[1])
        people_to_leave = int(data[2])
        train[index] -= people_to_leave

    command = input()

print(train)
