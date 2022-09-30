n = int(input())
elements = set()
for i in range(n):
    line = input().split()
    while line:
        elements.add(line.pop())
print('\n'.join(elements))
