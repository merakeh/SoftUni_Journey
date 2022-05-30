number_of_students = int(input())
failed_students = 0
average_grade_students = 0
good_grade_students = 0
excellent_grade_students = 0
sum_grade = 0

for student in range(1, number_of_students + 1):
    grade = float(input())
    sum_grade += grade
    if grade < 3:
        failed_students += 1
    elif 3 <= grade <= 3.99:
        average_grade_students += 1
    elif 4 <= grade <= 4.99:
        good_grade_students += 1
    elif 5 <= grade <= 6:
        excellent_grade_students += 1

avg_grade = sum_grade / number_of_students

top_students = excellent_grade_students / number_of_students * 100
good_grades = good_grade_students / number_of_students * 100
average_grade = average_grade_students / number_of_students * 100
failed = failed_students / number_of_students * 100

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {good_grades:.2f}%")
print(f"Between 3.00 and 3.99: {average_grade:.2f}%")
print(f"Fail: {failed:.2f}%")
print(f"Average: {avg_grade:.2f}")

