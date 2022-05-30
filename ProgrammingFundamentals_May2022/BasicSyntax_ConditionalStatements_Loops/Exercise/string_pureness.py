number = int(input())
is_pure = True

for i in range(number):
    text = input()

    if "," in text or "." in text or "_" in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")
