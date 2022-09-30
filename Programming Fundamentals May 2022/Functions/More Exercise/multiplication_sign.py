first = int(input())
second = int(input())
third = int(input())

num_list = [first, second, third]
negative_counter = 0
for digit in num_list:
    if digit < 0:
        negative_counter += 1
is_zero = False
for number in num_list:
    if number == 0:
        is_zero = True
        break

if is_zero:
    print("zero")
elif negative_counter % 2 != 0:
    print("negative")
elif negative_counter % 2 == 0:
    print("positive")

