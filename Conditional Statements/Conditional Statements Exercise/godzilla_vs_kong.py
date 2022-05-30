
budget = float(input())
actors = int(input())
clothes_price = float(input())
clothes_total = actors * clothes_price
decor = budget * 0.1

if actors > 150:
    clothes_total = clothes_total * 0.9

money_needed = decor + clothes_total

difference = abs(money_needed - budget)

if budget >= money_needed:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
