expected_sum_money = int(input())
total_count_transactions = 0
collected_money = 0
cash_money = 0
card_money = 0
cash_transactions = 0
card_transactions = 0
average_cash = 0
average_card = 0
input_line = input()
while input_line != "End":
    current_money = int(input_line)
    total_count_transactions += 1

    if total_count_transactions % 2 == 0 and current_money >= 10:
        card_money += current_money
        card_transactions += 1
        average_card = card_money / card_transactions
        print("Product sold!")
    elif total_count_transactions % 2 != 0 and current_money <= 100:
        cash_money += current_money
        cash_transactions += 1
        average_cash = cash_money / cash_transactions
        print("Product sold!")
    else:
        print("Error in transaction!")

    collected_money = cash_money + card_money

    if collected_money >= expected_sum_money:
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_card:.2f}")
        break

    input_line = input()

if input_line == "End":
    print("Failed to collect required money for charity.")
