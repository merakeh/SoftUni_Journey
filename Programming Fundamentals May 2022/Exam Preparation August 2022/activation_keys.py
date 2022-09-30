
some_string = input()

while True:
    command = input()

    if command == "Generate":
        break

    data = command.split('>>>')
    if data[0] == "Contains":
        substring = data[1]
        if substring in some_string:
            print(f"{some_string} contains {substring}")
        else:
            print("Substring not found!")

    elif data[0] == "Flip":
        word_case = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        substring = some_string[start_index:end_index]

        if word_case == "Upper":
            some_string = some_string[:start_index]+substring.upper()+some_string[end_index:]
            print(some_string)

        elif word_case == "Lower":
            some_string = some_string[:start_index]+substring.lower()+some_string[end_index:]
            print(some_string)

    elif data[0] == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])

        some_string = some_string[:start_index]+some_string[end_index:]
        print(some_string)

print(f"Your activation key is: {some_string}")