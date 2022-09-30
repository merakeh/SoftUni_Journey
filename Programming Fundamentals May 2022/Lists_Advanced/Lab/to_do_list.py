notes = 10 * [0]

while True:
    command = input()
    if command == "End":
        break

    #Takes values as a list
    tokens = command.split("-")
    # Creates an index from the first value in the list
    priority = int(tokens[0]) - 1
    # Takes the note from the list
    note = tokens[1]
    # Removes the index digit
    notes.pop(priority)
    # Inserts the note at the created index
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)
