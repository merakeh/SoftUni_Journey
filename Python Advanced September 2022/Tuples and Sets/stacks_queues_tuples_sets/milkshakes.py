from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_milk = deque([int(x) for x in input().split(', ')])

counter = 0

while chocolates and cups_milk and counter < 5:

    last_choco = chocolates.pop()
    first_milk = cups_milk.popleft()

    if last_choco <= 0 and first_milk <= 0:
        continue

    if last_choco <= 0:
        cups_milk.appendleft(first_milk)
        continue

    if first_milk <= 0:
        chocolates.append(last_choco)
        continue

    if last_choco == first_milk:
        counter += 1
    else:
        cups_milk.append(first_milk)
        chocolates.append(last_choco - 5)

if counter == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: ", end='')
    print(', '.join([str(x) for x in chocolates]))
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: ", end='')
    print(', '.join([str(x) for x in cups_milk]))
else:
    print("Milk: empty")
