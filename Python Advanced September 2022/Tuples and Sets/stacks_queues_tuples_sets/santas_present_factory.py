from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents_count = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and magic_level:

    last_box_materials = materials.pop()
    first_magic_level = magic_level.popleft()

    total_magic_level = last_box_materials * first_magic_level

    if total_magic_level == 150:
        presents_count["Doll"] += 1
    elif total_magic_level == 250:
        presents_count["Wooden train"] += 1
    elif total_magic_level == 300:
        presents_count["Teddy bear"] += 1
    elif total_magic_level == 400:
        presents_count["Bicycle"] += 1

    elif total_magic_level > 0:
        materials.append(last_box_materials + 15)
    elif total_magic_level < 0:
        materials.append(last_box_materials + first_magic_level)
    else:
        if last_box_materials == 0 and first_magic_level == 0:
            continue
        elif last_box_materials == 0:
            magic_level.appendleft(first_magic_level)
        elif first_magic_level == 0:
            materials.append(last_box_materials)

if (
        (presents_count["Doll"] > 0 and presents_count["Wooden train"] > 0)
        or (presents_count["Teddy bear"] > 0 and presents_count["Bicycle"] > 0)
):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials.reverse()
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for toy, quantity in sorted(presents_count.items()):
    if quantity > 0:
        print(f"{toy}: {quantity}")




