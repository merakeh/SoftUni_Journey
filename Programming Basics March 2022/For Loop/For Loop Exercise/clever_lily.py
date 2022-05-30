age_lily = int(input())
price_washing_machine = float(input())
toy_price = int(input())
toys_count = 0
birthday_money = 0
money_from_toys = 0
saved_money = 0
money_for_brother = 0

for number in range(1, age_lily + 1):
    if number % 2 != 0:
        toys_count += 1
    elif number % 2 == 0:
        birthday_money = birthday_money + 10 * (number / 2)
        money_for_brother += 1

money_from_toys = toys_count * toy_price - money_for_brother
saved_money = birthday_money + money_from_toys
difference = abs(saved_money - price_washing_machine)

if saved_money >= price_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
