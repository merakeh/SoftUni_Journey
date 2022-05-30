number_of_moves = int(input())
result = 0
count_to_nine = 0
count_to_nineteen = 0
count_to_twenty_nine = 0
count_to_thirty_nine = 0
count_to_fifty = 0
invalid_numbers = 0

for game in range(number_of_moves):
    current_number = int(input())
    if 0 <= current_number <= 9:
        result += current_number * 0.2
        count_to_nine += 1
    elif 10 <= current_number <= 19:
        result += current_number * 0.3
        count_to_nineteen += 1
    elif 20 <= current_number <= 29:
        result += current_number * 0.4
        count_to_twenty_nine += 1
    elif 30 <= current_number <= 39:
        result += 50
        count_to_thirty_nine += 1
    elif 40 <= current_number <= 50:
        result += 100
        count_to_fifty += 1

    if current_number < 0 or current_number > 50:
        result = result / 2
        invalid_numbers += 1

to_nine = count_to_nine / number_of_moves * 100
to_nineteen = count_to_nineteen / number_of_moves * 100
to_twenty_nine = count_to_twenty_nine / number_of_moves * 100
to_thirty_nine = count_to_thirty_nine / number_of_moves * 100
to_fifty = count_to_fifty / number_of_moves * 100
invalid = invalid_numbers / number_of_moves * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {to_nine:.2f}%")
print(f"From 10 to 19: {to_nineteen:.2f}%")
print(f"From 20 to 29: {to_twenty_nine:.2f}%")
print(f"From 30 to 39: {to_thirty_nine:.2f}%")
print(f"From 40 to 50: {to_fifty:.2f}%")
print(f"Invalid numbers: {invalid:.2f}%")
