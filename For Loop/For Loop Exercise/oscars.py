# actor_name = input()
# academy_points = float(input())
# number_of_point_givers = int(input())
# total_points = academy_points
#
# for number in range(1, number_of_point_givers + 1):
#     jury_name = input()
#     points = float(input())
#     total_points = total_points + (len(jury_name) * points) / 2
#     if total_points >= 1250.5:
#         break
#
# if total_points < 1250.5:
#     print(f"Sorry, {actor_name} you need {1250.5 - total_points} more!")
# else:
#     print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")

actor_name = input()
init_points = float(input())
count_people = int(input())

total_points = init_points
for i in range(1, count_people + 1):
    name = input()
    current_points = float(input())

    points = (len(name) * current_points) / 2
    total_points = total_points + points
    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    diff = abs(1250.5 - total_points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")