def replace_char(text):
    for char in text:
        while char * 2 in text:
            text = text.replace(char*2, char)
    return text


text_input = input()
print(replace_char(text_input))