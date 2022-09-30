import re

# Matching numbers
regex_pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
text = input()
matches = re.finditer(regex_pattern, text)

for match in matches:
    print(match.group(), end=" ")

# Matching names
names = input()
regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(regex, names)
print(' '.join(matches))

# Matching phone numbers
phones = input()
regex = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
matches = re.findall(regex, phones)
print(', '.join(matches))

# Matching dates
regex = r"\b(\d{2})([-\.\/])([A-Z][a-z]{2})\2(\d{4})\b"
text = input()
matches = re.findall(regex, text)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
