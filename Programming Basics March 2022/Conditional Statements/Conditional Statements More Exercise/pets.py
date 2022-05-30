from math import floor
from math import ceil
days_away = int(input())
food_prepared = int(input())
dog_food_a_day_kg = float(input())
cat_food_a_day_kg = float(input())
turtle_food_a_day_grams = float(input())

dog_food_grams = dog_food_a_day_kg * 1000
cat_food_grams = cat_food_a_day_kg * 1000

dog_food_needed = days_away * dog_food_grams
cat_food_needed = days_away * cat_food_grams
turtle_food_needed = days_away * turtle_food_a_day_grams

food_needed_grams = dog_food_needed + cat_food_needed + turtle_food_needed
food_needed_kg = food_needed_grams / 1000
difference = abs(food_needed_kg - food_prepared)

if food_needed_kg <= food_prepared:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")

