input_line = input()
adults = 0
kids = 0
money_toys = 0
sweater_money = 0

while input_line != "Christmas":
    age = int(input_line)
    if age <= 16:
        kids += 1
        money_toys += 5
    else:
        adults += 1
        sweater_money += 15

    input_line = input()

print(f"Number of adults: {adults}" )
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_toys}")
print(f"Money for sweaters: {sweater_money}")
