cats_count = int(input())

small_cats = 0
big_cats = 0
large_cats = 0
food_grams = 0

for cat in range(cats_count):
    food_for_day = float(input())
    food_grams += food_for_day

    if 100 <= food_for_day < 200:
        small_cats += 1
    elif 200 <= food_for_day < 300:
        big_cats += 1
    elif 300 <= food_for_day < 400:
        large_cats += 1

food_money = (food_grams / 1000) * 12.45
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {large_cats} cats.")
print(f"Price for food per day: {food_money:.2f} lv.")
