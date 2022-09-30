initial_text = input()
encrypted_text = ''

for char in initial_text:
    cipher_ord = ord(char) + 3
    cipher_char = chr(cipher_ord)
    encrypted_text += cipher_char

print(encrypted_text)