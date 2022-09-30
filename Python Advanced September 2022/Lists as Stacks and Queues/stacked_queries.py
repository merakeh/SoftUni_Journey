
stack = []
n = int(input())

for _ in range(n):
    query = input().split()
    command = query[0]

    if command == '1':
        stack.append(int(query[1]))
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4':
        print(min(stack))

while stack:
    item = stack.pop()
    if stack:
        print(item, end=', ')
    else:
        print(item)
