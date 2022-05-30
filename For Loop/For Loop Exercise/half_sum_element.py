import sys

count_of_numbers = int(input())
max_num = -sys.maxsize
sum_numbers = 0

for i in range(1, count_of_numbers + 1):
    num = int(input())
    sum_numbers = sum_numbers + num
    if num > max_num:
        max_num = num
sum_numbers = sum_numbers - max_num

if sum_numbers == max_num:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    diff = abs(sum_numbers - max_num)
    print("No")
    print(f"Diff = {diff}")
