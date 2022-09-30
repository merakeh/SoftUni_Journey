current_version = list(map(int, input().split('.')))

if current_version[2] == 9:
    if current_version[1] == 9:
        if current_version[0] == 9:
            exit
        print(f"{current_version[0] +1}.{0}.{0}")
    else:
        print(f"{current_version[0]}.{current_version[1] + 1}.{0}")
else:
    print(f"{current_version[0]}.{current_version[1]}.{current_version[2] + 1}")


# Given solution

# version = [int(number) for number in input().split(".")]
# version[-1] += 1
# for current_index in range(len(version) - 1, -1, -1):
#     if version[current_index] > 9:
#         version[current_index] = 0
#         if current_index - 1 >= 0:
#             version[current_index - 1] += 1
# print('.'.join(str(number) for number in version))
