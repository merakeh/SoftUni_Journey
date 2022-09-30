nums = input().split(', ')


def positive_numbers(number):
    return [positive for positive in number if int(positive) >= 0]


def negative_numbers(number):
    return [negative for negative in number if int(negative) < 0]


def even_numbers(number):
    return [even for even in number if int(even) % 2 == 0]


def odd_numbers(number):
    return [odd for odd in number if int(odd) % 2 != 0]


print(f"Positive: {', '.join(positive_numbers(nums))}")
print(f"Negative: {', '.join(negative_numbers(nums))}")
print(f"Even: {', '.join(even_numbers(nums))}")
print(f"Odd: {', '.join(odd_numbers(nums))}")

