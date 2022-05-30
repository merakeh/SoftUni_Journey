from math import ceil
fan_name = input()
budget = float(input())
beer_bottles = int(input())
chips_packages = int(input())

money_for_beer = beer_bottles * 1.20
price_a_package = money_for_beer * 0.45
total_for_chips = ceil(price_a_package * chips_packages)

total_sum = money_for_beer + total_for_chips
difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")
