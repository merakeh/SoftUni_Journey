
def forecast(*data):
    info_dict = {'Sunny': [], "Cloudy": [], "Rainy": []}
    for element in data:
        location = element[0]
        weather = element[1]

        if weather == "Sunny":
            info_dict[weather].append(location)
        elif weather == "Cloudy":
            info_dict[weather].append(location)
        elif weather == "Rainy":
            info_dict[weather].append(location)

    result = []

    for key, value in info_dict.items():
        value = sorted(value)

        if key == "Sunny":
            for each in value:
                result.append(f"{each} - Sunny")
        elif key == "Cloudy":
            for each in value:
                result.append(f"{each} - Cloudy")
        elif key == "Rainy":
            for each in value:
                result.append(f"{each} - Rainy")

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
