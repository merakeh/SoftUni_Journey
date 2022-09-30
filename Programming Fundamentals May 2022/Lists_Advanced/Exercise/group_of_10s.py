
numbers_to_sort = list(map(int, input().split(', ')))
nums = numbers_to_sort
for group_of_tens in range(1, len(numbers_to_sort)):
    if len(nums) <= 0:
        break
    filtered = list(filter(lambda x: x <= group_of_tens * 10, nums))
    for element in filtered:
        if element in nums:
            nums.remove(element)

    print(f"Group of {group_of_tens * 10}'s: {filtered}")

