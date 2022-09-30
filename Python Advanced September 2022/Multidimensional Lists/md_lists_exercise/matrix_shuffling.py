
def is_valid(row, col, command: list):
    for i in range(1, len(command)):
        command[i] = int(command[i])

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        return False

    if command[1] >= row or command[3] >= row or \
       command[2] >= col or command[4] >= col:
        print("Invalid input!")
        return False

    return True


r, c = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(r)]

line = input().split()

while line[0] != "END":

    if is_valid(r, c, line):

        # Storing the two elements that need to be swapped
        items = matrix[int(line[1])][int(line[2])], \
                matrix[int(line[3])][int(line[4])]

        # Swapping the elements
        matrix[int(line[3])][int(line[4])], matrix[int(line[1])][int(line[2])] = items

        # Printing the output
        for row_index in range(r):
            print(' '.join(matrix[row_index]))
        # print(matrix)

    line = input().split()
