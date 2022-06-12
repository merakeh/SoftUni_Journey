numbers = input().split(", ")
beggars = int(input())
result_list = []
counter_of_index = 0

numbers_as_integers = []
for element in numbers:
    numbers_as_integers.append(int(element))

while counter_of_index < beggars:
    sum_of_current_index = 0
    for current_beggar in range(counter_of_index, len(numbers_as_integers), beggars):
        sum_of_current_index += numbers_as_integers[current_beggar]
    result_list.append(sum_of_current_index)
    counter_of_index += 1
print(result_list)
