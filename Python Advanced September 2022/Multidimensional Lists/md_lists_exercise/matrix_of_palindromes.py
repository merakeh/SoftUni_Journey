
rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    palindrome_list = []
    for col in range(cols):
        palindrome = f"{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}"
        palindrome_list.append(palindrome)
    print(' '.join(palindrome_list))


