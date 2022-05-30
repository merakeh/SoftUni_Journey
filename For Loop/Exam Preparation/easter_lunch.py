easter_bread_count = int(input())
eggs_in_bulk = int(input())
cookies_kilograms = int(input())

eggs_count = eggs_in_bulk * 12
eggs_price = 4.35

easter_bread_sum = easter_bread_count * 3.2
eggs_total_price = eggs_in_bulk * eggs_price + eggs_count * 0.15
cookies_total_price = cookies_kilograms * 5.4

total_expenses = easter_bread_sum + eggs_total_price + cookies_total_price
print(f"{total_expenses:.2f}")
