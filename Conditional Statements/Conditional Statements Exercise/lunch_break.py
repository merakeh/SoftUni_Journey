from math import ceil
series = str(input())
episode_length = int(input())
break_time = int(input())

lunch = break_time * (1/8)
rest = break_time * (1/4)
free_time = break_time - (lunch + rest + episode_length)
time_for_series = break_time - (lunch + rest)

if time_for_series >= episode_length:
    free_time = break_time - (lunch + rest + episode_length)
    print(f"You have enough time to watch {series} and left with {ceil(free_time)} minutes free time.")
else:
    free_time = abs(break_time - (lunch + rest + episode_length))
    print(f"You don't have enough time to watch {series}, you need {ceil(free_time)} more minutes.")

