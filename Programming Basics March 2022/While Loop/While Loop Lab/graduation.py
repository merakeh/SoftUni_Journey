student_name = input()
current_class = 1
bad_tries = 0
is_failed = False
grade = 0

# Докато ученикът не е завършил 12 клас / current_class <= 12

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries == 2:
            is_failed = True
            break
        continue
    current_class += 1
    grade += current_grade

if is_failed:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average = grade / 12
    print(f"{student_name} graduated. Average grade: {average:.2f}")
