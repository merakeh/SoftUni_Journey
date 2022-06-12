operation = input()
first_num = int(input())
second_num = int(input())


def calculate(action, a, b):
    result = None
    if action == "multiply":
        result = a * b
    elif action == "divide":
        result = a / b
    elif action == "add":
        result = a + b
    elif action == "subtract":
        result = a - b
    return int(result)


print(calculate(operation, first_num, second_num))
