input_line = input()
is_full = False
total_tickets = 0
student_tickets = 0
standard_ticket = 0
kids_ticket = 0

while input_line != "Finish":
    movie_name = input_line
    capacity = int(input())
    count_tickets_current_movie = 0

    command_line = input()
    while command_line != "End":
        type_of_ticket = command_line
        count_tickets_current_movie += 1
        total_tickets += 1

        if type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "standard":
            standard_ticket += 1
        elif type_of_ticket == "kid":
            kids_ticket += 1

        if count_tickets_current_movie == capacity:
            break

        command_line = input()

    percent_full = count_tickets_current_movie / capacity * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    input_line = input()

percent_student = student_tickets / total_tickets * 100
percent_standard = standard_ticket / total_tickets * 100
percent_kids = kids_ticket / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
