first = int(input())
second = int(input())
third = int(input())


def sum_numbers(a, b):
    c = a + b
    return c


def subtract(a, b, d):
    e = sum_numbers(a, b) - d
    return e


print(subtract(first, second, third))
