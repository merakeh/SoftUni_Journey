import re

pattern = r"(\|([A-Z]{4,})\|)\:(\#[a-zA-Z]+\s[a-zA-Z]+\#)"

n = int(input())
valid_list = []
for inputs in range(n):
    text = input()
    match = re.search(pattern, text)
    if match:
        valid = match.group()
        boss_name, title = valid.split(":")
        boss_name = boss_name.strip("|")
        title = title.strip("#")

        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")

