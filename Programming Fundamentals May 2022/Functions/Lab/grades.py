grade = float(input())


def name_grade(number):
    name = None
    if 2 <= number < 3:
        name = "Fail"
    elif 3 <= number < 3.50:
        name = "Poor"
    elif 3.50 <= number < 4.50:
        name = "Good"
    elif 4.50 <= number < 5.50:
        name = "Very Good"
    elif 5.50 <= number <= 6:
        name = "Excellent"

    return name


print(name_grade(grade))

