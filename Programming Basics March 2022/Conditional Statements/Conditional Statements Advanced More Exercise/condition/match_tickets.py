budget = float(input())
ticket_category = input()
number_of_people = int(input())
transport_money = 0
ticket_price = 0

if ticket_category == "Normal":
    ticket_price = 249.99
elif ticket_category == "VIP":
    ticket_price = 499.99

if 1 <= number_of_people <= 4:
    transport_money = budget * 0.75
elif number_of_people <= 9:
    transport_money = budget * 0.6
elif number_of_people <= 24:
    transport_money = budget * 0.5
elif number_of_people <= 49:
    transport_money = budget * 0.4
elif number_of_people >= 50:
    transport_money = budget * 0.25

total_needed = ticket_price * number_of_people + transport_money
difference = abs(budget - total_needed)

if budget >= total_needed:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
