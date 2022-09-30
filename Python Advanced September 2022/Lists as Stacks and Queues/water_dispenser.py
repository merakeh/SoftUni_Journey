from collections import deque
water_quantity = int(input())

people = deque()

while True:
    person = input()
    if person == "Start":
        break

    people.append(person)

while True:
    command = input().split()
    if command[0] == "End":
        break

    if command[0] == "refill":
        water_quantity += int(command[1])
    else:
        current_person = people.popleft()
        if int(command[0]) <= water_quantity:
            print(f"{current_person} got water")
            water_quantity -= int(command[0])
        else:
            print(f"{current_person} must wait")
            if people:
                people.popleft()

print(f"{water_quantity} liters left")