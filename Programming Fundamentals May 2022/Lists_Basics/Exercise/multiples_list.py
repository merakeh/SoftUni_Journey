factor = int(input())
count = int(input())
my_list = []
dividend = 1
while len(my_list) < count:
    if dividend % factor == 0:
        my_list.append(dividend)
    dividend += 1

print(my_list)

