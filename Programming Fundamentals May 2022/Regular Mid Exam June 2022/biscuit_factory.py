from math import floor
biscuits_person_day = int(input())
workers_count = int(input())
production_competing_factory = int(input())

production_per_day = biscuits_person_day * workers_count

production_per_month = production_per_day * 20 + (production_per_day * 0.75) * 10
difference_in_production = production_per_month - production_competing_factory

print(f"You have produced {floor(production_per_month)} biscuits for the past month.")

if difference_in_production > 0:
    percent_difference = difference_in_production / production_competing_factory * 100
    print(f"You produce {percent_difference:.2f} percent more biscuits.")
elif difference_in_production < 0:
    percent_difference = difference_in_production / production_competing_factory * 100
    print(f"You produce {abs(percent_difference):.2f} percent less biscuits.")
