import sys

command = input()
max_number = -sys.maxsize

while command != "Stop":
    current_number = int(command)
    if current_number > max_number:
        max_number = current_number
    command = input()
print(max_number)

# Това се използва за минимално число, по аналогично условие

# import sys
# command = input()
# min_number = sys.maxsize
#
# while command != "Stop":
#     current_number = int(command)
#     if current_number < min_number:
#         min_number = current_number
#     command = input()
# print(min_number)
