from collections import deque

sequence = input().split()
q = deque()
for ch in sequence:

    if ch in "/*-+":
        while len(q) > 1:
            first = q.popleft()
            second = q.popleft()
            result = 0

            if ch == '+':
                result = first + second
            elif ch == '-':
                result = first - second
            elif ch == '*':
                result = first * second
            elif ch == '/':
                result = first // second

            q.appendleft(result)
    else:
        q.append(int(ch))

print(q.popleft())