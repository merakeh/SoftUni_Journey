n = int(input())

bracket = ")"
is_balanced = True
for i in range(n):
    text = input()
    if text == ")" or text == "(":
        if text == bracket:
            is_balanced = False
            break
        else:
            bracket = text
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
