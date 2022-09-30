number = input()
digits = []
for digit in number:
    digits.append(digit)

digits.sort(reverse=True)

for i in digits:
    print(''.join(i), end='')


