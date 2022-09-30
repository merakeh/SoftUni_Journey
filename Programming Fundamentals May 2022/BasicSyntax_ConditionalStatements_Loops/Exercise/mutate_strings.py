first = input()
second = input()
last_string = first

for letter in range(len(first)):
    left_part = second[:letter+1]
    right_part = first[letter+1::]
    current_text = left_part + right_part
    if current_text == last_string:
        continue
    last_string = current_text
    print(current_text)

