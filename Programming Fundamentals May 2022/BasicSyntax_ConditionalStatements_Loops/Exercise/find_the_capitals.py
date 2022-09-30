string = input()
capitals = []
for letter in range(len(string)):
    if string[letter].isupper():

        capitals.append(letter)

print(capitals)