list_of_words = input().split()
palindrome = input()
found_palindromes = []

for word in list_of_words:
    if word == word[::-1]:
        found_palindromes.append(word)

print(found_palindromes)
print(f"Found palindrome {list_of_words.count(palindrome)} times")