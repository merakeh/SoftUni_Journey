current_password = input()

#
# def is_valid(password):
#     validity = None
#     if 6 >= len(password) <= 10:
#         validity = True
#     else:
#         validity = False
#         print("Password must be between 6 and 10 characters")
#     if password.isalnum():
#         validity = True
#     else:
#         validity = False
#         print("Password must consist only of letters and digits")
#
#     counter_of_digits = 0
#     for char in password:
#         if char.isdigit():
#             counter_of_digits += 1
#         if counter_of_digits >= 2:
#             validity = True
#         else:
#             validity = False
#             print("Password must have at least 2 digits")
#
#     if validity:
#         print("Password is valid")
#
#
# is_valid(current_password)


def is_correct_length(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def is_letters_and_digits(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def has_two_digits(password):
    counter_of_digits = 0
    for char in password:
        if char.isdigit():
            counter_of_digits += 1
    if counter_of_digits >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


if is_correct_length(current_password) and is_letters_and_digits(current_password) and has_two_digits(current_password):
    print("Password is valid")

