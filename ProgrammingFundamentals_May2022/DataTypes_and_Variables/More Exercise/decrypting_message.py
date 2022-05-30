key = int(input())
lines = int(input())
decrypted_symbol = ''

for symbol in range(lines):
    letter = input()
    decrypted_symbol = ord(letter) + key
    print(chr(decrypted_symbol), end='')
print()
