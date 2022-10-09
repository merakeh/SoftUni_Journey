symbols = ["-", ",", ".", "!", "?"]

with open("./text.txt", 'r') as text_file:
    text_lines = text_file.readlines()

for line in range(0, len(text_lines), 2):
    for symbol in symbols:
        text_lines[line] = text_lines[line].replace(symbol, '@')

    print(*text_lines[line].split()[::-1])

