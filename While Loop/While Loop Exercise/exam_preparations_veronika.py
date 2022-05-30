bad_tries = int(input())

sum_grades = 0
count_grades = 0
last_problem = ""
count_bad_grades = 0
is_failed = False
input_line = input()
while input_line != "Enough":
    grade = int(input())
    if grade <= 4:
        count_bad_grades += 1

    last_problem = input_line
    count_grades = count_grades + 1
    sum_grades = sum_grades + grade

    if bad_tries == count_bad_grades:
        is_failed = True
        break
    input_line = input()

if is_failed:
    print(f"You need a break, {count_bad_grades} poor grades.")
else:
    average_grade = sum_grades / count_grades
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")
