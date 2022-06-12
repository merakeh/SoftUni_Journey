def data_types(input_type, line):
    if input_type == "int":
        print(int(line) * 2)
    elif input_type == "real":
        print(f"{float(line) * 1.5:.2f}")
    elif input_type == "string":
        print(f"${line}$")


data_type = input()
command = input()

data_types(data_type, command)
