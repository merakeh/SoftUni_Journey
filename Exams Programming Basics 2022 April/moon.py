from math import ceil
speed = float(input())
moon_earth = 384400
fuel_per_hundred_km = float(input())

total_kms = moon_earth * 2
time_both_ways = total_kms / speed
total_time = time_both_ways + 3

fuel_needed = (fuel_per_hundred_km * total_kms) / 100

print(ceil(total_time))
print(round(fuel_needed))
