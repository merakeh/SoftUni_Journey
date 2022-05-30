capacity = 255
total_liters = 0
num = int(input())

for buckets in range(num):
    poured_liters = int(input())
    if capacity - poured_liters >= 0:
        capacity -= poured_liters
    else:
        print("Insufficient capacity!")
        continue

    total_liters += poured_liters

print(total_liters)
