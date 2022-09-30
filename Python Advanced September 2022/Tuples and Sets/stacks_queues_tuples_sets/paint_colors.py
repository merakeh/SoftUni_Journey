from collections import deque
substrings = deque(input().split())
colors = []

given_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']

while substrings:

    first = substrings.popleft()
    last = substrings.pop() if substrings else ""
    current_word = first + last

    if current_word in given_colors:
        colors.append(current_word)
        continue

    current_word = last + first
    if current_word in given_colors:
        colors.append(current_word)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        substrings.insert(len(substrings) // 2, first)
    if last:
        substrings.insert(len(substrings) // 2, last)

for color in colors:

    if color == "orange":
        if "red" not in colors or "yellow" not in colors:
            colors.remove(color)
    if color == "purple":
        if "red" not in colors or "blue" not in colors:
            colors.remove(color)
    if color == "green":
        if "yellow" not in colors or "blue" not in colors:
            colors.remove(color)

print(colors)