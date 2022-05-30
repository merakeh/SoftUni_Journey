
vacation_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

price_puzzle = puzzles * 2.6
price_talking_doll = talking_dolls * 3
price_teddy_bear = teddy_bears * 4.1
price_minion = minions * 8.2
price_truck = trucks * 2

total_number_toys = puzzles + talking_dolls + teddy_bears + minions + trucks
total_price = price_puzzle + price_talking_doll + price_teddy_bear + price_minion + price_truck


if total_number_toys >= 50:
    total_price = total_price * 0.75

money_after_rent = total_price * 0.9

diff = abs(vacation_price - money_after_rent)
if money_after_rent >= vacation_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
