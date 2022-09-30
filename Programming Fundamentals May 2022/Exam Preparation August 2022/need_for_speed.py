
number_of_cars = int(input())
cars_dict = {}

for i in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars_dict[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break

    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        if fuel > cars_dict[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['fuel'] -= fuel
            cars_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars_dict[car]['mileage'] >= 100000:
            del cars_dict[car]
            print(f"Time to sell the {car}!")

    if command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        initial_fuel = cars_dict[car]['fuel']
        cars_dict[car]['fuel'] += fuel
        if cars_dict[car]['fuel'] > 75:
            cars_dict[car]['fuel'] = 75
        print(f"{car} refueled with {cars_dict[car]['fuel'] - initial_fuel} liters")

    if command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])

        cars_dict[car]['mileage'] -= kilometers
        if cars_dict[car]['mileage'] < 10000:
            cars_dict[car]['mileage'] = 10000
            continue
        print(f"{car} mileage decreased by {kilometers} kilometers")

for vehicle, info in cars_dict.items():
    print(f"{vehicle} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")