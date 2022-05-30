kilometers = int(input())
day_or_night = input()
price = 0

if kilometers < 20:
    if day_or_night == "day":
        price = 0.7 + kilometers * 0.79
    elif day_or_night == "night":
        price = 0.7 + kilometers * 0.9
elif 20 <= kilometers < 100:
    price = kilometers * 0.09
else:
    price = kilometers * 0.06
print(f"{price:.2f}")
