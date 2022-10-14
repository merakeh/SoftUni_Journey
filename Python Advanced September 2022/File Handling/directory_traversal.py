import os
directory = input()
result = []
extensions = {}

for file_name in os.listdir(directory):
    file = os.path.join(directory, file_name)

    if os.path.isfile(file):
        extension = file_name.split('.')[-1]

        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(file_name)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}\n")

    for file in sorted(files):
        result.append(f"- - - {file}\n")

with open("./report.txt", 'w') as report:
    report.write(''.join(result))
