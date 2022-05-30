record_sec = float(input())
distance_m = float(input())
time_sec_m = float(input())

ivan_time = distance_m * time_sec_m
water_resistance = (distance_m // 15) * 12.5

total_time_ivan = ivan_time + water_resistance
difference = abs(total_time_ivan - record_sec)

if total_time_ivan < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time_ivan:.2f} seconds.")
elif total_time_ivan >= record_sec:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")

