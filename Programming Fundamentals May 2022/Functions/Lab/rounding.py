a_list = input().split()
new_list = []
for num in a_list:
    new_list.append(float(num))

print(list(map(round, new_list)))
