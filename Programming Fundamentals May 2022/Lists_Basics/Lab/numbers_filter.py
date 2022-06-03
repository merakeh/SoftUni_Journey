n = int(input())
numbers = []
filtered = []
for i in range(n):
    current = int(input())
    numbers.append(current)

category = input()

if category == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered.append(num)
elif category == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered.append(num)
elif category == "negative":
    for num in numbers:
        if num < 0:
            filtered.append(num)
elif category == "positive":
    for num in numbers:
        if num >= 0:
            filtered.append(num)

print(filtered)
