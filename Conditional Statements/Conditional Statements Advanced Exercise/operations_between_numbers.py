number1 = int(input())
number2 = int(input())
operator = input()
result = 0
odd_even = ""

if operator == "+":
    result = number1 + number2
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
elif operator == "-":
    result = number1 - number2
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
elif operator == "*":
    result = number1 * number2
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
elif operator == "/":
    if number2 == 0:
        result = False
    else:
        result = number1 / number2
elif operator == "%":
    if number2 == 0:
        result = False
    else:
        result = number1 % number2

if operator == "+" or operator == "-" or operator == "*":
    print(f"{number1} {operator} {number2} = {result} - {odd_even}")
elif not result:
    print(f"Cannot divide {number1} by zero")
elif operator == "/":
    print(f"{number1} / {number2} = {result:.2f}")
elif operator == "%":
    print(f"{number1} % {number2} = {result}")

