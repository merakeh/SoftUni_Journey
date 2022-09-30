import re

sentence = input()
pattern = r'(?<=\s)([a-z0-9]+[\-\.\_a-z0-9]*@[a-z\-]+(\.[a-z]+)+)\b'

matches = re.findall(pattern, sentence)

for match in matches:
    print(match[0])
