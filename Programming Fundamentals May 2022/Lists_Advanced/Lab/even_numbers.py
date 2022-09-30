numbers = list(map(int, input().split(', ')))

# Return only the indices of even numbers in the list
indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(indices)
