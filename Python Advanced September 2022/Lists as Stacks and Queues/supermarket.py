from collections import deque

queue = deque()
while True:
    customer = input()
    if customer == "End":
        break

    if customer == "Paid":
        print('\n'.join(queue))
        queue.clear()
    else:
        queue.append(customer)

print(f"{len(queue)} people remaining.")