inheritance = float(input())
year_to_live_to = int(input())
ivan_age = 17
money = inheritance

for year in range(1800, year_to_live_to + 1):
    ivan_age += 1

    if year % 2 == 0:
        money = money - 12000
    else:
        money = money - (12000 + 50 * ivan_age)

if money > 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")
