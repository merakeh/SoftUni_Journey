will_he_sleep = input()
starting_height = 5364
difference = 8848 - 5364
is_successful = False
days_count = 1

while will_he_sleep != "END":
    current_climb = int(input())
    if will_he_sleep == "Yes":
        days_count += 1

    difference -= current_climb
    if difference < 0:
        is_successful = True
        break

    if days_count == 5:
        break

    will_he_sleep = input()

if is_successful:
    print(f"Goal reached for {days_count} days!")
else:
    print("Failed!")
    print(8848 - difference)
