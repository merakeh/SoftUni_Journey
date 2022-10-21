
def start_spring(**kwargs):
    new_dict = {}
    result = []
    for value, key in kwargs.items():
        if key not in new_dict:
            new_dict[key] = []
        new_dict[key].append(value)
    sorted_dict = sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, objects in sorted_dict:
        result.append(f"{key}:")

        for value in sorted(objects):
            result.append(f"-{value}")
    return '\n'.join(result)


example_objects = {
    "Water Lilly": "flower",
    "Swifts": "bird",
    "Callery Pear": "tree",
    "Swallows": "bird",
    "Dahlia": "flower",
    "Tulip": "flower",
}

print(start_spring(**example_objects))
