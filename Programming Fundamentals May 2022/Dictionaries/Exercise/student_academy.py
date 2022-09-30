
def average_grade(grades: list):
    average = sum(grades) / len(grades)
    return average


n = int(input())
students = {}

for i in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

for stud, gradee in students.items():
    if average_grade(gradee) >= 4.50:
        print(f"{stud} -> {average_grade(gradee):.2f}")
