line = input()
symbols = {}

for i in line:
    if i not in symbols:
        symbols[i] = 0
    symbols[i] += 1

sorted_keys = sorted(symbols.keys())
for element in sorted_keys:
    print(f"{element}: {symbols[element]} time/s")

