import re

pattern = r'\b_[A-Za-z0-9]+\b'
text = input()

result = re.findall(pattern, text)
final_result = []

for match in result:
    final_result.append(match[1:])

print(','.join(final_result))
