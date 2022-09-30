n = int(input())


def tribonacci(num):
    first = 1
    second = 1
    third = 2
    current = 0
    for i in range(3, num):
        current = first + second + third
        first = second
        second = third
        third = current
    return current


if n == 1:
    print("1")
if n == 2:
    print("1 1")
if n == 3:
    print("1 1 2")
if n > 3:
    print(f"1 1 2 ", end='')
    for digit in range(4, n + 1):
        print(f"{tribonacci(digit)} ", end='')
