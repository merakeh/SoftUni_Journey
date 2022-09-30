import re

n = int(input())

for i in range(n):
    data = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
    match = re.match(pattern, data)

    if not match:
        print("Invalid barcode")
    else:
        digit_pattern = r'\d'
        product_group = re.findall(digit_pattern, match.group())
        if not product_group:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(product_group)}")

