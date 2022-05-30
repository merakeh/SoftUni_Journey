from math import floor
from math import ceil

days_away = int(input())
food = int(input())

food_left = food

for deer in range(3):
    current_deer = float(input())
    food_left = food_left - (current_deer * days_away)

if food_left >= 0:
    print(f"{floor(food_left)} kilos of food left.")
else:
    food_left = abs(food_left)
    print(f"{ceil(food_left)} more kilos of food are needed.")
