
def func_executor(*args):
    result = ''
    for func in args:
        name_func = func[0].__name__
        output_func = func[0](*func[1])
        result += f"{name_func} - {output_func}\n"

    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
