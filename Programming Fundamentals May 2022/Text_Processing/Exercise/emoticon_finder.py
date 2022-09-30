input_text = input()
possible_emoticons = []
for index in range(len(input_text)):
    char = input_text[index]
    if char == ':' and input_text[index + 1] != ' ':
        possible_emoticons.append(char + input_text[index + 1])
print('\n'.join(possible_emoticons))