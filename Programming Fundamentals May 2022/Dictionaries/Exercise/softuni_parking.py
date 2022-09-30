n = int(input())
parking_database = {}

for i in range(n):
    car_data = input().split()
    if car_data[0] == "register":
        username, license_plate_number = car_data[1], car_data[2]

        if username in parking_database:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking_database[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif car_data[0] == "unregister":
        username = car_data[1]
        if username not in parking_database:
            print(f"ERROR: user {username} not found")
        else:
            parking_database.pop(username)
            print(f"{username} unregistered successfully")


for car, plate in parking_database.items():
    print(f"{car} => {plate}")

