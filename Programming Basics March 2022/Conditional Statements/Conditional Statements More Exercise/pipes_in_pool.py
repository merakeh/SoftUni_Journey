pool_volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours_missing = float(input())

pipe_one = pipe_one_debit * hours_missing
pipe_two = pipe_two_debit * hours_missing
total_litres = pipe_one + pipe_two

total_percents = total_litres / pool_volume * 100
pipe_one_percents = (pipe_one / total_litres) * 100
pipe_two_percents = (pipe_two / total_litres) * 100

difference = abs(total_litres - pool_volume)

if total_litres <= pool_volume:
    print(f"The pool is {total_percents:.2f}% full. Pipe 1: {pipe_one_percents:.2f}%. Pipe 2: {pipe_two_percents:.2f}%.")
else:
    print(f"For {hours_missing} hours the pool overflows with {difference:.2f} liters.")
