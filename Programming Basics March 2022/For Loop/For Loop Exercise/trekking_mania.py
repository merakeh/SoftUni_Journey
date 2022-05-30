number_of_groups = int(input())
total_count_of_people = 0
mussala = 0
montblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0

for group in range(number_of_groups):
    count_of_climbers = int(input())
    if count_of_climbers <= 5:
        mussala += count_of_climbers
    elif 6 <= count_of_climbers <= 12:
        montblanc += count_of_climbers
    elif 13 <= count_of_climbers <= 25:
        kilimandjaro += count_of_climbers
    elif 26 <= count_of_climbers <= 40:
        k2 += count_of_climbers
    elif count_of_climbers >= 41:
        everest += count_of_climbers
    total_count_of_people += count_of_climbers

mussala_climbers = mussala / total_count_of_people * 100
montblanc_climbers = montblanc / total_count_of_people * 100
kilimandjaro_climbers = kilimandjaro / total_count_of_people * 100
k2_climbers = k2 / total_count_of_people * 100
everest_climbers = everest / total_count_of_people * 100

print(f"{mussala_climbers:.2f}%")
print(f"{montblanc_climbers:.2f}%")
print(f"{kilimandjaro_climbers:.2f}%")
print(f"{k2_climbers:.2f}%")
print(f"{everest_climbers:.2f}%")
