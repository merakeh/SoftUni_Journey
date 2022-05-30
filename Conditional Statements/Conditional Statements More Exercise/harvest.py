import math

total_harvested_area = int(input())
grapes_kilo_of_one_sq_m = float(input())
liters_wine_needed = int(input())
count_workers = int(input())

grapes_harvested = total_harvested_area * grapes_kilo_of_one_sq_m
grapes_produced = grapes_harvested * 0.4
wine_produced = grapes_produced / 2.5
difference = abs(liters_wine_needed - wine_produced)
liters_per_person = difference / count_workers

if wine_produced < liters_wine_needed:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine_produced)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(liters_per_person)} liters per person.")
