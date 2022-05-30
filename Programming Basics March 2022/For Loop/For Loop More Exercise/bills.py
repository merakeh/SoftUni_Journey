months = int(input())

other_expenses = 0  #(water (= 20) + internet (= 15) + electricity) * 1.2
sum_electricity = 0

for month in range(months):
    current_electricity = float(input())
    sum_electricity += current_electricity
    other_expenses = other_expenses + ((current_electricity + 20 + 15) * 1.2)

sum_water = 20 * months
sum_internet = 15 * months
total_expenses = sum_electricity + sum_water + sum_internet + other_expenses
average_expenses = total_expenses / months

print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {other_expenses:.2f} lv")
print(f"Average: {average_expenses:.2f} lv")
