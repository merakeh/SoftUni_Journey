budget = float(input())
season = input()
accommodation = ""
price = 0
place = ""
if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.6
else:
    accommodation = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        place = "Alaska"
    elif season == "Winter":
        place = "Morocco"

print(f"{place} - {accommodation} - {price:.2f}")
