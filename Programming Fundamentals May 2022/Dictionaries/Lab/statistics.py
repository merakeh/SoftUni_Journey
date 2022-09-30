
command = input()
info_dict = {}
while True:
    if command == "statistics":
        break

    products = command.split(': ')
    key = products[0]
    value = products[1]
    if key not in info_dict.keys():
        info_dict[key] = int(value)
    else:
        info_dict[key] += int(value)

    command = input()

print("Products in stock:")

print('\n'.join(f"- {item}: {info_dict[item]}" for item in info_dict))
print(f"Total Products: {len(info_dict)}")
print(f"Total Quantity: {sum(info_dict.values())}")



