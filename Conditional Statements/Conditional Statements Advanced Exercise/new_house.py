flower_type = input()
count = int(input())
budget = int(input())
price = 0
total = 0

if flower_type == "Roses":
    price = 5
    total = price * count
    if count > 80:
        total = total * 0.9
elif flower_type == "Dahlias":
    price = 3.8
    total = price * count
    if count > 90:
        total = total * 0.85
elif flower_type == "Tulips":
    price = 2.8
    total = price * count
    if count > 80:
        total = total * 0.85
elif flower_type == "Narcissus":
    price = 3
    total = price * count
    if count < 120:
        total = total * 1.15
elif flower_type == "Gladiolus":
    price = 2.5
    total = price * count
    if count < 80:
        total = total * 1.2

difference = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with\
 {count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
