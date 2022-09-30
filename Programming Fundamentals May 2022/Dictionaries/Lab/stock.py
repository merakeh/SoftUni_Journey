products = input().split(' ')
searched_products = input().split(' ')
prod_dict = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    prod_dict[key] = int(value)

for product in searched_products:
    if product in prod_dict.keys():
        print(f"We have {prod_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

