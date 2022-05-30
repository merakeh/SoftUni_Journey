from math import floor

number_of_tournaments = int(input())
initial_points = int(input())
total_points = initial_points
winner_position = 0

for position in range(number_of_tournaments):
    place_achieved = input()
    if place_achieved == "W":
        total_points += 2000
        winner_position += 1
    elif place_achieved == "F":
        total_points += 1200
    elif place_achieved == "SF":
        total_points += 720

average_of_collected_points = (total_points - initial_points) / number_of_tournaments
percent_won_tournaments = winner_position / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_of_collected_points)}")
print(f"{percent_won_tournaments:.2f}%")
