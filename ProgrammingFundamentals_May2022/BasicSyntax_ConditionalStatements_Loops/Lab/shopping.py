budget = int(input())
input_line = input()
money = 0
while input_line != "End":
    money_spent = int(input_line)
    money += money_spent
    if money > budget:
        print("You went in overdraft!")
        break
    input_line = input()
else:
    print("You bought everything needed.")

