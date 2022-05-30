rest_days = int(input())
work_days = 365 - rest_days
workday_play_minutes = 63
rest_day_play_minutes = 127
norm_per_year = 30000

total_playtime_per_year = work_days * workday_play_minutes + rest_days * rest_day_play_minutes
difference = abs(norm_per_year - total_playtime_per_year)
hours = difference // 60
minutes = difference % 60

if total_playtime_per_year >= norm_per_year:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
