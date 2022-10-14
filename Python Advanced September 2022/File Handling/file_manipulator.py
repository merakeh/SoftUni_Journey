import os

while True:
    info = input().split('-')
    if info[0] == "End":
        break

    if info[0] == "Create":
        file = open(f"./{info[1]}", 'w')
        file.close()
    elif info[0] == "Add":
        with open(f"./{info[1]}", 'a') as file:
            file.write(f"{info[2]}\n")
    elif info[0] == "Replace":
        try:
            with open(f"./{info[1]}", 'r+') as file:
                text = file.readlines()

                for idx in range(len(text)):
                    text[idx] = text[idx].replace(info[2], info[3])

                file.write(''.join(text))

        except FileNotFoundError:
            print("File not found!")
    elif info[0] == "Delete":
        try:
            os.remove(f"./{info[1]}")
        except FileNotFoundError:
            print("File not found!")
