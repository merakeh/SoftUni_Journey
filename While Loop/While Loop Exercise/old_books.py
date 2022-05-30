searched_book = input()

current_book = input()
is_found = False
book_count = 0
while current_book != "No More Books":
    if current_book == searched_book:
        is_found = True
        break

    book_count = book_count + 1
    current_book = input()

if is_found:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
