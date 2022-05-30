number_of_people = int(input())
season = input()
price_a_person = 0

if number_of_people <= 5:
    if season == "spring":
        price_a_person = 50
    elif season == "summer":
        price_a_person = 48.50
    elif season == "autumn":
        price_a_person = 60
    elif season == "winter":
        price_a_person = 86
else:
    if season == "spring":
        price_a_person = 48
    elif season == "summer":
        price_a_person = 45
    elif season == "autumn":
        price_a_person = 49.5
    elif season == "winter":
        price_a_person = 85

group_price = price_a_person * number_of_people

if season == "summer":
    group_price = group_price * 0.85
elif season == "winter":
    group_price = group_price * 1.08

print(f"{group_price:.2f} leva.")
