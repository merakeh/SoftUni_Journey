first_sequence = input().split(', ')
second_sequence = input().split(', ')

substring_list = []

result = [element for element in first_sequence if element in second_sequence]

for element in first_sequence:
    for word in second_sequence:
        if element in word and element not in substring_list:
            substring_list.append(element)

print(substring_list)
