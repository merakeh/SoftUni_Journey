text = input().lower()
dictionary = {}
for char in text:
    if char not in dictionary:
        if char == " ":
            continue
        dictionary[char] = 0
    dictionary[char] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
