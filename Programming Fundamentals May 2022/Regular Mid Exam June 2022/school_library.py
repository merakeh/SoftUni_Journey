shelf_with_books = input().split('&')


def swap_books(some_list, index_one, index_two):
    some_list[index_one], some_list[index_two] = some_list[index_two], some_list[index_one]
    return some_list


command = input()
while command != "Done":

    sequence = command.split(' | ')
    action = sequence[0]
    book_name = sequence[1]

    if action == "Add Book":
        if book_name in shelf_with_books:
            command = input()
            continue
        shelf_with_books.insert(0, book_name)
    elif action == "Take Book":
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)
        else:
            command = input()
            continue
    elif action == "Swap Books":
        if sequence[1] in shelf_with_books and sequence[2] in shelf_with_books:
            first_index = shelf_with_books.index(sequence[1])
            second_index = shelf_with_books.index(sequence[2])
            swap_books(shelf_with_books, first_index, second_index)
    elif action == "Insert Book":
        if book_name in shelf_with_books:
            command = input()
            continue
        shelf_with_books.append(book_name)
    elif action == "Check Book":
        index = int(sequence[1])
        if index < 0 or index > len(shelf_with_books):
            command = input()
            continue
        print(shelf_with_books[index])

    command = input()

print(', '.join(shelf_with_books))
