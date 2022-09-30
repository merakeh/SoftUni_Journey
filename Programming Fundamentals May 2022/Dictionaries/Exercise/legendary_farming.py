useful_items = {"shards": 0, "fragments": 0, "motes": 0}
useless_items = {}
is_obtained = False
items = input().split(' ')

while True:
    for index in range(0, len(items), 2):
        key = items[index + 1].lower()
        value = int(items[index])
        if key in useful_items.keys():
            useful_items[key] += value
        else:
            if key not in useless_items:
                useless_items[key] = 0
            useless_items[key] += value

        if useful_items["shards"] >= 250:
            is_obtained = True
            print("Shadowmourne obtained")
            useful_items["shards"] -= 250
        elif useful_items["fragments"] >= 250:
            is_obtained = True
            print("Valanyr obtained")
            useful_items["fragments"] -= 250
        elif useful_items["motes"] >= 250:
            is_obtained = True
            print("Dragonwrath obtained")
            useful_items["motes"] -= 250

        if is_obtained:
            break
    if is_obtained:
        break
    items = input().split(' ')

for material, quantity in useful_items.items():
    print(f"{material}: {quantity}")
for material, quantity in useless_items.items():
    print(f"{material}: {quantity}")
