numbers = [float(x) for x in input().split()]
num_dict = {}

for num in numbers:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1

for key, value in num_dict.items():
    print(f"{key:.1f} - {value} times")
    