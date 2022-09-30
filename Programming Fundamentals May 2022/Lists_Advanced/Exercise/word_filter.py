words = input().split()

result = [word for word in words if len(word) % 2 == 0]
for index in range(len(result)):
    print(result[index])


# Given solution

# words = input().split()
# filtered_words = [word for word in words if len(word) % 2 == 0]
# print('\n'.join(filtered_words))

# print('\n'.join([word for word in input().split() if len(word) % 2 == 0]))
