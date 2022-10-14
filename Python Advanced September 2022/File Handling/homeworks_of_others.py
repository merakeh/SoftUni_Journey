from os import walk
from os import listdir, path
for root, dirs, file in walk('.'):
    print(file)


def traversal(file_path):
    for el in listdir(file_path):
        if path.isdir(path.join(file_path, el)):
            traversal(path.join(file_path, el))
        else:
            file_info = el.split('.')
            if file_info[1] not in files:
                files[file_info[1]] = []
            files[file_info[1]].append(el)


files = {}
traversal('.')
for extension, file in sorted(files.items()):
    print('.' + extension)
    file.sort()
    for name in file:
        print(f'- - -  {name}')
