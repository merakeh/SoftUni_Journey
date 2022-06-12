char_one = input()
char_two = input()
char_list = []


def get_character_in_range(first, second):
    for char in range(ord(first) + 1, ord(second)):
        char_list.append(chr(char))
    return char_list


result = get_character_in_range(char_one, char_two)
print(" ".join(result))


# This is a second solution to the problem

# char_one = input()
# char_two = input()
#
# char_list = []
#
#
# def get_character_in_range(first, second):
#     for char in range(ord(first) + 1, ord(second)):
#         char_list.append(chr(char))
#
#     for element in char_list:
#         print(element, end=' ')
#
#
# get_character_in_range(char_one, char_two)




