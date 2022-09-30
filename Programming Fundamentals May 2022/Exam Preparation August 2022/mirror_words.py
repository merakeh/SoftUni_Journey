import re

string = input()
regex = r"(\@|\#)([a-zA-Z]){3,}\1\1([a-zA-Z]){3,}\1"

matches = re.finditer(regex, string)
pairs = []
not_mirrored = []

for match in matches:
    current_text = match.group()
    length = len(current_text) // 2
    first_word = current_text[:length]
    second_word = current_text[length:]

    if first_word == second_word[::-1]:
        pairs.append(first_word+second_word)
    else:
        not_mirrored.append(first_word+second_word)


if not matches:
    print("No word pairs found!")
else:
    print(f"{len(not_mirrored)+len(pairs)} word pairs found!")
if matches and not pairs:
    print("No mirror words!")
if pairs:
    print("The mirror words are:")
    for pair in pairs:
        if pair[0] == '@':
            first, second = pair[1:-1].split('@@')
        elif pair[0] == '#':
            first, second = pair[1:-1].split('##')
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 #                 THIS DOESNT WORK
        # print(''.join(f"{first} <=> {second}"))
