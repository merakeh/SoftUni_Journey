list_nums = input().split(", ")


def is_palindrome(num):
    return num == num[::-1]


for element in list_nums:
    print(is_palindrome(element))
