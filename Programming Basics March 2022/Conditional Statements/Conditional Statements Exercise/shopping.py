
budget = float(input())
videocards = int(input())
procesors = int(input())
ram_memory = int(input())

videocard_price = videocards * 250
procesors_price = (videocard_price * 0.35) * procesors
ram_memory_price = (videocard_price * 0.1) * ram_memory

total_price = videocard_price + procesors_price + ram_memory_price

if videocards > procesors:
    total_price = total_price * 0.85

difference = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
