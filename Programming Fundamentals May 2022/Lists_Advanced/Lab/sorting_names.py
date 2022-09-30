given_names = input().split(', ')

sorted_list = sorted(given_names, key=lambda x: (-len(x), x))
print(sorted_list)