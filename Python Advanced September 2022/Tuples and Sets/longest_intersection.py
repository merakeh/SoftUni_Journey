def generate_sequence(range_nums):
    start, end = [int(x) for x in range_nums.split(',')]
    return set(range(start, end + 1))


n = int(input())

longest_intersection = set()

for i in range(n):
    line_parts = input().split('-')
    first_set = generate_sequence(line_parts[0])
    second_set = generate_sequence(line_parts[1])
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")