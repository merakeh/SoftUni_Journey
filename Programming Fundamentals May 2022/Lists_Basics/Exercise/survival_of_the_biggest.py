input_line = input().split()
n = int(input())
numbers = []
for element in input_line:
    numbers.append(int(element))

for num in range(n):
    numbers.remove(min(numbers))

for digit in range(len(numbers) - 1):
    print(numbers[digit], end=", ")
print(numbers[-1])
