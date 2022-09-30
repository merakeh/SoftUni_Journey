from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = 0

while bees and nectar:

    first_bee = bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= first_bee:
        current_operator = symbols.popleft()
        if current_operator == '+':
            honey += abs(first_bee + last_nectar)
        elif current_operator == '-':
            honey += abs(first_bee - last_nectar)
        elif current_operator == '*':
            honey += abs(first_bee * last_nectar)
        elif current_operator == '/':
            honey += abs(first_bee / last_nectar)
    else:
        bees.appendleft(first_bee)

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

