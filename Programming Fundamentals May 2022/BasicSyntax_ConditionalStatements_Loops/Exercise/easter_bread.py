budget = float(input())
one_kg_flour_price = float(input())

one_pack_eggs_price = one_kg_flour_price * 0.75
milk_price = one_kg_flour_price * 1.25 * 0.25
loaf_price = one_kg_flour_price + one_pack_eggs_price + milk_price

current_bread_count = 0
money_left = budget
colored_eggs_count = 0

while money_left > loaf_price:
    current_bread_count += 1
    colored_eggs_count += 3
    if current_bread_count % 3 == 0:
        colored_eggs_count -= (current_bread_count - 2)
    money_left -= loaf_price
print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {money_left:.2f}BGN left.")

