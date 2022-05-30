will_he_sleep = input()
current_height = 5364
everest_height = 8848
days_climbing = 1
has_succeeded = False

while will_he_sleep != "END":
    climbed_meters = int(input())
    current_height += climbed_meters
    if will_he_sleep == "Yes":
        days_climbing += 1

    if current_height >= 8848:
        has_succeeded = True
        break

    if days_climbing == 5:
        break
    will_he_sleep = input()

if has_succeeded:
    print(f"Goal reached for {days_climbing} days!")
else:
    print("Failed!")
    print(current_height)

     # Решение от общия чат
# base_camp = 5364
# everest = 8848
#
# days = 1
#
# while True:
#     night = input()
#     if night == "Yes":
#         days += 1
#     if days > 5 or night == "END":
#         break
#     meters = int(input())
#     base_camp += meters
#     if base_camp >= everest:
#         break
#
# if base_camp >= everest:
#     print(f"Goal reached for {days} days!")
# else:
#     print("Failed!\n"
#           f"{base_camp}")
