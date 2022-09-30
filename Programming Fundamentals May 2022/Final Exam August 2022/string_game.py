
string = input()

while True:
    commands = input().split()
    if commands[0] == "Done":
        break

    action = commands[0]
    if action == "Change":
        char = commands[1]
        replacement = commands[2]

        for letter in string:
            if letter == char:
                string = string.replace(letter, replacement)
        print(string)

    elif action == "Includes":
        substring = commands[1]
        if substring in string:
            print("True")
        else:
            print("False")

    elif action == "End":
        substring = commands[1]
        if string.endswith(substring):
            print("True")
        else:
            print("False")

    elif action == "Uppercase":
        string = string.upper()
        print(string)

    elif action == "FindIndex":
        char = commands[1]
        index = string.index(char)
        print(index)

    elif action == "Cut":
        start_index = int(commands[1])
        count = int(commands[2])
        end = start_index + count
        string = string[start_index:end]
        print(string)
