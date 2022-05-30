destination = input()

while destination != "End":
    minimum_budget = float(input())
    collected_money = 0
    while collected_money < minimum_budget:
        savings = float(input())
        collected_money += savings
    print(f"Going to {destination}!")
    destination = input()

