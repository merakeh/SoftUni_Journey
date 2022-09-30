
input_line = input().split(' ')
result = {}
for element in range(0, len(input_line), 2):
    key = input_line[element]
    value = int(input_line[element + 1])
    result[key] = value

print(result)
