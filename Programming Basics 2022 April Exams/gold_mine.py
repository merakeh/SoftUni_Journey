number_of_locations = int(input())


for location in range(number_of_locations):
    daily_expected_average = float(input())
    days_on_location = int(input())

    extraction_sum = 0
    avg_extraction = 0
    for day in range(days_on_location):
        extraction_a_day = float(input())
        extraction_sum += extraction_a_day
        avg_extraction = extraction_sum / days_on_location

    insufficiency = daily_expected_average - avg_extraction

    if avg_extraction >= daily_expected_average:
        print(f"Good job! Average gold per day: {avg_extraction:.2f}.")
    else:
        print(f"You need {insufficiency:.2f} gold.")
