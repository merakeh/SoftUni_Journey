n = int(input())
parking = set()
for i in range(n):
    direction, number = input().split(', ')
    if direction == "IN":
        parking.add(number)
    elif direction == "OUT":
        if number in parking:
            parking.remove(number)

if parking:
    print('\n'.join(parking))
else:
    print("Parking Lot is Empty")