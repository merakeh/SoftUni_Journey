from collections import deque


def replace_chars(word, character):
    if character in word:
        word = word.replace(character, '')
    return word


vowels = deque(input().split())
consonants = input().split()
is_found = False

flowers = ['rose', 'tulip', 'lotus', 'daffodil']

while vowels and consonants:
    vowel = vowels.popleft()
    last_cons = consonants.pop()

    for idx in range(len(flowers)):
        flowers[idx] = replace_chars(flowers[idx], vowel)
        if flowers[idx] == '':
            is_found = True
            break
        flowers[idx] = replace_chars(flowers[idx], last_cons)
        if flowers[idx] == '':
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print("Cannot find any word!")
else:
    index_ch = flowers.index('')
    if index_ch == 0:
        print("Word found: rose")
    if index_ch == 1:
        print("Word found: tulip")
    if index_ch == 2:
        print("Word found: lotus")
    if index_ch == 3:
        print("Word found: daffodil")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")


