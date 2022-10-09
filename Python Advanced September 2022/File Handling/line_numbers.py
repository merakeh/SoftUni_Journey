symbols = ["-", ",", ".", "!", "?", "\'"]

with open("./text.txt", 'r') as text_file:
    text = text_file.readlines()

for line in range(len(text)):
    # Setting the counter to 0 for each sentence
    symbol_counter = 0
    for symbol in symbols:
        symbol_counter += text[line].count(symbol)

    # Using a comprehension to take out the spaces and to count only alphabetical chars
    chars_count = len([el for el in text[line] if el.isalpha()])

    print(f"Line {line + 1}: {text[line]} ({chars_count})({symbol_counter})")

