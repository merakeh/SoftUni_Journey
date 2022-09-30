
# for i in range(4):
#     initial_input = input().split(':')
#     identifier = initial_input[1]
#     students_dict[identifier] = {"name": initial_input[0], "course": initial_input[2]}
#
# searched_course = ' '.join(input().split('_'))
#
# for key, value in students_dict.items():
#     if value['course'] == searched_course:
#         print(f"{value['name']} - {key}")
#

students_dict = {}

command = input()
while ":" in command:
    info = command.split(':')
    name, id, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    command = input()

searched_course = ' '.join(command.split('_'))

for key, value in students_dict.items():
    if key == searched_course:
        for id, name in value.items():
            print(f"{name} - {id}")

