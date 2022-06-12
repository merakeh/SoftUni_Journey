number = int(input())

string = str(number)
odd_sum = 0
even_sum = 0
for num in string:
    if int(num) % 2 == 0:
        even_sum += int(num)
    else:
        odd_sum += int(num)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
