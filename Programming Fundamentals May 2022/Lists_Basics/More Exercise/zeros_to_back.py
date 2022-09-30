string_of_numbers = list(map(int, input().split(", ")))

for number in string_of_numbers:
    if number == 0:
        string_of_numbers.remove(0)
        string_of_numbers.append(0)
print(string_of_numbers)
