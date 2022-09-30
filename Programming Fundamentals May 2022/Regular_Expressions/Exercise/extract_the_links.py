import re

pattern = r"((w{3})\.([A-z0-9\-])+(\.[a-z]+)+)"
valid_links = []

sentence = input()

while sentence:
    match = re.search(pattern, sentence)
    if match:
        valid_links.append(match[0])
    sentence = input()

for valid_url in valid_links:
    print(valid_url)
