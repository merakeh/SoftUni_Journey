from collections import deque

n = int(input())
pumps = deque()

for i in range(n):
    pump_info = [int(x) for x in input().split()]
    pumps.append(pump_info)

for attempt in range(n):
    tank = 0
    is_failed = False
    for fuel, distance in pumps:
        tank += fuel

        if distance > tank:
            is_failed = True
            break
        else:
            tank -= distance

    if is_failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
