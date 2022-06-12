product = input()
quantity = int(input())


def total_owed(order, count):
    price = None
    if order == "coffee":
        price = 1.50
    elif order == "coke":
        price = 1.40
    elif order == "water":
        price = 1.00
    elif order == "snacks":
        price = 2.00
    return count * price


print(f"{total_owed(product, quantity):.2f}")

