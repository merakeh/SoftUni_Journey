from collections import deque

seats = input().split(', ')
first_seq = deque(map(int, input().split(', ')))
second_seq = list(map(int, input().split(', ')))

rotations = 0
seated_matches = []

while len(seated_matches) < 3 and rotations < 10:
    first_num = first_seq.popleft()
    last_num = second_seq.pop()
    ascii_char = chr(first_num + last_num)
    rotations += 1

    if f"{first_num}{ascii_char}" in seats:
        if f"{first_num}{ascii_char}" in seated_matches:
            continue
        seated_matches.append(f"{first_num}{ascii_char}")
    elif f"{last_num}{ascii_char}" in seats:
        if f"{last_num}{ascii_char}" in seated_matches:
            continue
        seated_matches.append(f"{last_num}{ascii_char}")
    else:
        first_seq.append(first_num)
        second_seq.insert(0, last_num)

print(f"Seat matches: {', '.join(seated_matches)}")
print(f"Rotations count: {rotations}")

