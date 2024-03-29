
def palindrome(word: str, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    first, last = word[index], word[-1 - index]
    if first != last:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


print(palindrome("abcccvba", 0))
print(palindrome("peter", 0))