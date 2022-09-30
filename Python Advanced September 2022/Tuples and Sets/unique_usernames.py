n = int(input())
some_set = set()
for _ in range(n):
    line = input()
    some_set.add(line)

print('\n'.join(some_set))
