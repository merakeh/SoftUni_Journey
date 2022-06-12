values = input()
value_list = values.split(" ")
new_list = []
for i in range(len(value_list)):
    element = int(value_list[i]) * -1
    new_list.append(element)

print(new_list)
