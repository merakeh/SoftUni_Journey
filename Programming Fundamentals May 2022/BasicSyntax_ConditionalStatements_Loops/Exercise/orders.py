number_of_orders = int(input())
total = 0

for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    order = capsules_per_day * capsule_price * days
    total += order
    print(f"The price for the coffee is: ${order:.2f}")
print(f"Total: ${total:.2f}")
