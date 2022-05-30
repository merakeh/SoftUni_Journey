number_of_days = int(input())
sum_litres = 0
sum_degrees = 0

for day in range(1, number_of_days + 1):
    litres = float(input())
    degrees = float(input())

    sum_litres += litres
    sum_degrees += degrees * litres

average_degrees = sum_degrees / sum_litres

print(f"Liter: {sum_litres:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")

