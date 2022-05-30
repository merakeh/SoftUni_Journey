number = int(input())
string_number = str(number)
first = int(string_number[-1])
second = int(string_number[-2])
third = int(string_number[-3])

for first_number in range(1, first + 1):
    for second_number in range(1, second + 1):
        for third_number in range(1, third + 1):
            result = first_number * second_number * third_number
            print(f"{first_number} * {second_number} * {third_number} = {result};")
