people_in_a_group = int(input())
nights = int(input())
transport_cards = int(input())
museum_tickets = int(input())

sleep = nights * 20
transport = transport_cards * 1.60
museums = museum_tickets * 6
expenses_for_one = sleep + transport + museums
group_expenses = expenses_for_one * people_in_a_group

total = group_expenses * 1.25
print(f"{total:.2f}")
