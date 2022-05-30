from math import floor

breed = input()
cat_gender = input()
human_months = 0
is_invalid = False

if cat_gender == "m":
    if breed == "British Shorthair":
        human_months = 13 * 12
    elif breed == "Siamese":
        human_months = 15 * 12
    elif breed == "Persian":
        human_months = 14 * 12
    elif breed == "Ragdoll":
        human_months = 16 * 12
    elif breed == "American Shorthair":
        human_months = 12 * 12
    elif breed == "Siberian":
        human_months = 11 * 12
    else:
        is_invalid = True

elif cat_gender == "f":
    if breed == "British Shorthair":
        human_months = 14 * 12
    elif breed == "Siamese":
        human_months = 16 * 12
    elif breed == "Persian":
        human_months = 15 * 12
    elif breed == "Ragdoll":
        human_months = 17 * 12
    elif breed == "American Shorthair":
        human_months = 13 * 12
    elif breed == "Siberian":
        human_months = 12 * 12
    else:
        is_invalid = True

cat_months = floor(human_months / 6)

if is_invalid:
    print(f"{breed} is invalid cat!")
else:
    print(f"{cat_months} cat months")
