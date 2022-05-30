season = input()
km_per_month = float(input())
monthly_salary = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        monthly_salary = km_per_month * 0.75
    elif season == "Summer":
        monthly_salary = km_per_month * 0.90
    elif season == "Winter":
        monthly_salary = km_per_month * 1.05
elif km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        monthly_salary = km_per_month * 0.95
    elif season == "Summer":
        monthly_salary = km_per_month * 1.10
    elif season == "Winter":
        monthly_salary = km_per_month * 1.25
elif km_per_month <= 20000:
    monthly_salary = km_per_month * 1.45

seasonal_salary = (monthly_salary * 4) * 0.9
print(f"{seasonal_salary:.2f}")
