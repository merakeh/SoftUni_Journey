from math import floor

hours_needed = int(input())
days = int(input())
workers_count = int(input())

hours_for_work = (days * 0.9) * 8
extra_hours = (days * 2) * workers_count
total_hours = hours_for_work + extra_hours
difference = abs(hours_needed - total_hours)

if total_hours >= hours_needed:
    print(f"Yes!{floor(difference)} hours left.")
else:
    print(f"Not enough time!{floor(difference)} hours needed.")
