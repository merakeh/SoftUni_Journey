number = int(input())
divisor_count = 0
is_prime = True
if number <= 1:
    is_prime = False

for i in range(number, 1, -1):
    if number % i == 0:
        divisor_count += 1
    if divisor_count > 1:
        is_prime = False
        break

print(is_prime)
