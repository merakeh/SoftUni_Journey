jury = int(input())
input_line = input()
total_grade_sum = 0
grade_counter = 0

while input_line != "Finish":
    task_grade_sum = 0
    task_name = input_line
    for number_of_grades in range(1, jury + 1):
        grade = float(input())
        task_grade_sum += grade
        grade_counter += 1

    task_average = task_grade_sum / jury
    total_grade_sum += task_grade_sum

    print(f"{task_name} - {task_average:.2f}.")
    input_line = input()

final_grade = total_grade_sum / grade_counter
print(f"Student's final assessment is {final_grade:.2f}.")
