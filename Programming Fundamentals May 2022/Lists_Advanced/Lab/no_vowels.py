some_text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [ch for ch in some_text if ch.lower() not in vowels]
print(''.join(result))
