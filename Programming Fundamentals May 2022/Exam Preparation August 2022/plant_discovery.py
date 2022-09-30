
n = int(input())

plants_dict = {}
average_rating = 0
# Create a dictionary for the plants and their rarity
for iteration in range(n):
    plant_name, rarity = input().split("<->")
    plants_dict[plant_name] = {"rarity": rarity, "rating": []}

command = input()
while command != "Exhibition":
    action, info = command.split(': ')
    data = info.split(' - ')

    if data[0] not in plants_dict:
        print('error')
        command = input()
        continue

    if action == "Rate":
        plant, rating = info.split(' - ')
        plants_dict[plant]['rating'].append(int(rating))
    elif action == "Update":
        plant, new_rarity = info.split(' - ')
        plants_dict[plant]['rarity'] = new_rarity
    elif action == "Reset":
        plants_dict[info]['rating'].clear()

    for element in plants_dict:
        if len(plants_dict[data[0]]['rating']) != 0:
            average_rating = sum(plants_dict[data[0]]['rating']) / len(plants_dict[data[0]]['rating'])

    command = input()


def find_average(some_list: list):
    if len(some_list) > 0 and sum(some_list) != 0:
        average = sum(some_list) / len(some_list)
    else:
        average = 0
    return average


print("Plants for the exhibition:")
for plant, info in plants_dict.items():
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {find_average(info['rating']):.2f}")

