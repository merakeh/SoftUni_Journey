sequence = input().split()
text = input()
message = []

for number in sequence:
    current_index = 0
    for digit in number:
        current_index += int(digit)

    current_index = current_index % len(text)
    message.append(text[current_index])
    text = text.replace(text[current_index], "", 1)

print("".join(message))

