n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for number in range(n):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif 200 <= current_num <= 399:
        p2 += 1
    elif 400 <= current_num <= 599:
        p3 += 1
    elif 600 <= current_num <= 799:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

percent1 = p1 / n * 100
percent2 = p2 / n * 100
percent3 = p3 / n * 100
percent4 = p4 / n * 100
percent5 = p5 / n * 100
print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")
print(f"{percent4:.2f}%")
print(f"{percent5:.2f}%")
