
sequence = input()
opening_brackets = []
balanced = True
for ch in sequence:
    if ch in '[{(':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
        break
    else:
        last_opening = opening_brackets.pop()
        if f"{last_opening}{ch}" not in "(){}[]":
            balanced = False
            break

if balanced and not opening_brackets:
    print("YES")
else:
    print("NO")
