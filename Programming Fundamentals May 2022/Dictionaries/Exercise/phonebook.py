phone_book = {}
current_person = input()

while "-" in current_person:
    contact_name, phone_number = current_person.split('-')
    phone_book[contact_name] = phone_number
    current_person = input()

for search in range(int(current_person)):
    searched_name = input()
    if searched_name in phone_book.keys():
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
