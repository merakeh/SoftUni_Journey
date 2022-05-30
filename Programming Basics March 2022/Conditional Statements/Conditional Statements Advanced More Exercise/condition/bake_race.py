count_juniors = int(input())
count_seniors = int(input())
trace_type = input()
junior_price = 0
senior_price = 0

if trace_type == "trail":
    junior_price = 5.5
    senior_price = 7
elif trace_type == "cross-country":
    junior_price = 8
    senior_price = 9.5
    if (count_seniors + count_juniors) >= 50:
        junior_price = junior_price * 0.75
        senior_price = senior_price * 0.75
elif trace_type == "downhill":
    junior_price = 12.25
    senior_price = 13.75
elif trace_type == "road":
    junior_price = 20
    senior_price = 21.5

sum_money = (count_juniors * junior_price + count_seniors * senior_price) * 0.95
print(f"{sum_money:.2f}")
