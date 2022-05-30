hours = int(input())
minutes = int(input())
total_minutes = hours * 60 + minutes +15

hours_result = total_minutes // 60
minutes_result = total_minutes % 60

if hours_result > 23:
    hours_result = 0

if minutes_result < 10:
    print(f"{hours_result}:0{minutes_result}")
else:
    print(f"{hours_result}:{minutes_result}")
