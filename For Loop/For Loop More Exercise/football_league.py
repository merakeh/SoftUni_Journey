stadium_capacity = int(input())
fan_count = int(input())
a = 0
b = 0
v = 0
g = 0


for person in range(fan_count):
    sector = input()
    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1

sector_A_percent = a / fan_count * 100
sector_B_percent = b / fan_count * 100
sector_V_percent = v / fan_count * 100
sector_G_percent = g / fan_count * 100
all_fans_percent = fan_count / stadium_capacity * 100

print(f"{sector_A_percent:.2f}%")
print(f"{sector_B_percent:.2f}%")
print(f"{sector_V_percent:.2f}%")
print(f"{sector_G_percent:.2f}%")
print(f"{all_fans_percent:.2f}%")

