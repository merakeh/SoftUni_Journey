budget = float(input())
season = input()

car_class = ""
price_car = 0
type_of_car = ""

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        price_car = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        price_car = budget * 0.8
else:
    car_class = "Luxury class"
    type_of_car = "Jeep"
    price_car = budget * 0.9

print(car_class)
print(f"{type_of_car} - {price_car:.2f}")
