divisor = int(input())
boundary = int(input())

for i in range(boundary, 1, -1):
    largest = i % divisor
    if largest == 0:
        print(i)
        break

