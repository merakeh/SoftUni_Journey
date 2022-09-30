n, m = ([int(x) for x in input().split()])
set_one = set()
set_two = set()

for i in range(n + m):
    num = int(input())
    if i < n:
        set_one.add(num)
    elif i < m + n:
        set_two.add(num)

result = set_one.intersection(set_two)
print("\n".join([str(x) for x in result]))
