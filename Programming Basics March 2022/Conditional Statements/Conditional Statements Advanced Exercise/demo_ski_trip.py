days_of_stay = int(input())
type_of_accommodation = input()
evaluation = input()
price_a_night = 0
total = 0

if type_of_accommodation == "room for one person":
    price_a_night = 18
    total = price_a_night * (days_of_stay - 1)
elif type_of_accommodation == "apartment":
    price_a_night = 25
    total = price_a_night * (days_of_stay - 1)
    if days_of_stay < 10:
        total = total * 0.7
    elif 10 <= days_of_stay < 15:
        total = total * 0.65
    else:
        total = total * 0.5
elif type_of_accommodation == "president apartment":
    price_a_night = 35
    total = price_a_night * (days_of_stay - 1)
    if days_of_stay < 10:
        total = total * 0.9
    elif 10 <= days_of_stay < 15:
        total = total * 0.85
    else:
        total = total * 0.8


if evaluation == "positive":
    total = total * 1.25
elif evaluation == "negative":
    total = total * 0.9

print(f"{total:.2f}")
