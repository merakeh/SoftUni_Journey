contract_duration = input()
type_of_contract = input()
mobile_internet = input()
number_of_months = int(input())
initial_price = 0

if contract_duration == "one":
    if type_of_contract == "Small":
        initial_price = 9.98
    elif type_of_contract == "Middle":
        initial_price = 18.99
    elif type_of_contract == "Large":
        initial_price = 25.98
    elif type_of_contract == "ExtraLarge":
        initial_price = 35.99
elif contract_duration == "two":
    if type_of_contract == "Small":
        initial_price = 8.58
    elif type_of_contract == "Middle":
        initial_price = 17.09
    elif type_of_contract == "Large":
        initial_price = 23.59
    elif type_of_contract == "ExtraLarge":
        initial_price = 31.79

if mobile_internet == "yes":
    if initial_price <= 10:
        initial_price += 5.5
    elif initial_price <= 30:
        initial_price += 4.35
    else:
        initial_price += 3.85

total_price = initial_price * number_of_months

if contract_duration == "two":
    total_price = total_price * 0.9625

print(f"{total_price:.2f} lv.")
