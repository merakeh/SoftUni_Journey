factor = int(input())
count = int(input())
my_list = []
for i in range(factor, factor * count + 1, factor):
    my_list.append(i)
print(my_list)
