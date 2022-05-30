count_bad_tries = int(input())
input_line = input()

bad_tries = 0
sum_grade = 0
number_of_tasks = 0
is_failed = False

while input_line != "Enough":
    task_grade = int(input())
    if task_grade <= 4:
        bad_tries += 1

    number_of_tasks += 1
    sum_grade += task_grade
    last_problem = input_line

    if bad_tries == count_bad_tries:
        is_failed = True
        break

average_grade = sum_grade / number_of_tasks

if is_failed:
    print(f"You need a break, {bad_tries} poor grades.")
elif input_line == "Enough":
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {input_line}")
