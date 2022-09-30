n = int(input())
students = {}

for i in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    average = sum(grades)/(len(grades))
    grades = [str(f"{x:.2f}") for x in grades]
    print(f"{student} -> {' '.join(grades)} (avg: {average:.2f})")
