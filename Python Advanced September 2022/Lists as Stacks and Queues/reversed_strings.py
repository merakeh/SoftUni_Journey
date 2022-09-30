
text = list(input())
result = []

for i in range(len(text)):
    result += text.pop()

print(''.join(result))