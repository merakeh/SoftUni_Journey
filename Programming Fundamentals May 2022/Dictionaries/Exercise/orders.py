
products = {}

command = input()

while command != "buy":
    info_products = command.split(' ')
    name, price, quantity = info_products[0], float(info_products[1]), int(info_products[2])
    if name not in products:
        products[name] = {"price": price, "quantity": 0}
    products[name]["price"] = price
    products[name]["quantity"] += quantity

    command = input()

for product, details in products.items():
    print(f"{product} -> {details['price'] * details['quantity']:.2f}")