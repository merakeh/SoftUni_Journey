budget = float(input())
season = input()
destination = ""
housing = ""
price_housing = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        housing = "Camp"
        price_housing = budget * 0.3
    elif season == "winter":
        housing = "Hotel"
        price_housing = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        housing = "Camp"
        price_housing = budget * 0.4
    elif season == "winter":
        housing = "Hotel"
        price_housing = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    housing = "Hotel"
    price_housing = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{housing} - {price_housing:.2f}")
