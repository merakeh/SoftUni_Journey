width = int(input())
length = int(input())

count_pieces = width * length

input_line = input()
while input_line != "STOP":
    current_pieces = int(input_line)
    count_pieces -= current_pieces

    if count_pieces <= 0:
        break
    input_line = input()

if count_pieces > 0:
    print(f"{count_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(count_pieces)} pieces more.")
