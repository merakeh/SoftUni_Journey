first_number = int(input())
final_number = int(input())

magic_number = int(input())
combination_count = 0
is_equal = False

for x in range(first_number, final_number + 1):
    for y in range(first_number, final_number + 1):
        combination_count += 1
        if x + y == magic_number:
            is_equal = True
            break
    if is_equal:
        break

if is_equal:
    print(f"Combination N:{combination_count} ({x} + {y} = {magic_number})")
else:
    print(f"{combination_count} combinations - neither equals {magic_number}")


