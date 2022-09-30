first_string, second_string = input().split()
total_sum = 0

len_first = len(first_string)
len_second = len(second_string)

if len_first > len_second:
    for index in range(len_second):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len_second, len_first):
        total_sum += ord(first_string[index])
elif len_first < len_second:
    for index in range(len_first):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len_first, len_second):
        total_sum += ord(second_string[index])
else:
    for index in range(len_first):
        total_sum += ord(first_string[index]) * ord(second_string[index])

print(total_sum)
