def sum_values(name):
    result = 0
    for ch in name:
        result += ord(ch)
    return result


n = int(input())
odd_nums = set()
even_nums = set()

for row in range(1, n + 1):
    line = input()
    sum_chars = sum_values(line)
    divided = sum_chars // row

    if divided % 2 == 0:
        even_nums.add(divided)
    else:
        odd_nums.add(divided)

sum_even_set = sum(even_nums)
sum_odd_set = sum(odd_nums)

if sum_even_set == sum_odd_set:
    union = odd_nums.union(even_nums)
    print(', '.join([str(x) for x in union]))
elif sum_odd_set > sum_even_set:
    diff = odd_nums.difference(even_nums)
    print(', '.join([str(x) for x in diff]))
else:
    sym_diff = odd_nums.symmetric_difference(even_nums)
    print(', '.join([str(x) for x in sym_diff]))
