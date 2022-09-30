
letters = input().split(', ')
# char_ord = []
# for char in letters:
#     char_ord.append(ord(char))
#
# result = dict(zip(letters, char_ord))
# print(result)

result = {char: ord(char) for char in letters}

print(result)


