info_vehicles = input().split(">>")
total_tax_collected = 0

for vehicle in range(len(info_vehicles)):
    info_current = info_vehicles[vehicle].split()
    car_type = info_current[0]
    years_to_tax = int(info_current[1])
    kilometers_traveled = int(info_current[2])

    valid_types = ["family", "heavyDuty", "sports"]
    if car_type not in valid_types:
        print("Invalid car type.")
        continue

    initial_tax = 0
    current_car_tax = 0
    if car_type == "family":
        initial_tax = 50
        current_car_tax = (initial_tax - years_to_tax * 5) + (kilometers_traveled // 3000) * 12
    elif car_type == "heavyDuty":
        initial_tax = 80
        current_car_tax = (initial_tax - years_to_tax * 8) + (kilometers_traveled // 9000) * 14
    elif car_type == "sports":
        initial_tax = 100
        current_car_tax = (initial_tax - years_to_tax * 9) + (kilometers_traveled // 2000) * 18

    print(f"A {car_type} car will pay {current_car_tax:.2f} euros in taxes.")

    total_tax_collected += current_car_tax

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
