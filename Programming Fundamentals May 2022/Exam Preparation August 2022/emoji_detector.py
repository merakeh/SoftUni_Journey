import re

# Use regex to find emojis and numbers
pattern_emojis = r"(::|\*\*)([A-Z]{1}[a-z]{2,})(\1)"
pattern_nums = r'\d'

# Get input from the user
piece_of_string = input()

# cool_threshold is 1 to be able to use multiplication
cool_threshold = 1
count_of_emojis = 0

# Find only the numbers and calculate the cool threshold of the text
numbers = re.findall(pattern_nums, piece_of_string)

for index in range(len(numbers)):
    cool_threshold *= int(numbers[index])

# Find valid emojis in the text
valid_emojis = re.findall(pattern_emojis, piece_of_string)

# Print the first part of the output
print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")

# Calculate coolness of each emoji and print only those above the threshold
for info in valid_emojis:
    word = info[1]
    coolness = 0
    for letter in word:
        coolness += ord(letter)

    if coolness >= cool_threshold:
        print(info[0] + info[1] + info[2])
