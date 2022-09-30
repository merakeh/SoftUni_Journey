from math import floor
biscuit_person_a_day = int(input())
workers_count = int(input())
competing_monthly_production = int(input())
monthly_production = 0

for day in range(1, 31):
    production_daily = workers_count * biscuit_person_a_day
    if day % 3 == 0:
        production_daily = production_daily * 0.75
    monthly_production += production_daily
print(f"You have produced {floor(monthly_production)} biscuits for the past month.")

if monthly_production < competing_monthly_production:
    percentage_diff = (competing_monthly_production - monthly_production) / competing_monthly_production * 100
    print(f"You produce {percentage_diff:.2f} percent less biscuits.")
else:
    percentage_diff = (monthly_production - competing_monthly_production) / competing_monthly_production * 100
    print(f"You produce {percentage_diff:.2f} percent more biscuits.")
