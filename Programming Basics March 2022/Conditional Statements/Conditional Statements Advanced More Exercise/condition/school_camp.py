season = input()
gender = input()
students_count = int(input())
nights_count = int(input())

night_price = 0
sport = ""

if season == "Winter":
    if gender == "boys":
        night_price = 9.6
        sport = "Judo"
    elif gender == "girls":
        night_price = 9.6
        sport = "Gymnastics"
    elif gender == "mixed":
        night_price = 10
        sport = "Ski"

elif season == "Spring":
    if gender == "boys":
        night_price = 7.2
        sport = "Tennis"
    elif gender == "girls":
        night_price = 7.2
        sport = "Athletics"
    elif gender == "mixed":
        night_price = 9.5
        sport = "Cycling"

elif season == "Summer":
    if gender == "boys":
        night_price = 15
        sport = "Football"
    elif gender == "girls":
        night_price = 15
        sport = "Volleyball"
    elif gender == "mixed":
        night_price = 20
        sport = "Swimming"

total_price = students_count * nights_count * night_price

if students_count >= 50:
    total_price = total_price * 0.5
elif 20 <= students_count < 50:
    total_price = total_price * 0.85
elif 10 <= students_count < 20:
    total_price = total_price * 0.95

print(f"{sport} {total_price:.2f} lv.")
