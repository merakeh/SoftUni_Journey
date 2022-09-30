
command = input()
courses = {}
while command != "end":
    course_name, student_name = command.split(' : ')

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for course, names in courses.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")

