first_team_wins = 0
first_team_loses = 0
first_team_draws = 0

for games in range(3):
    current_match = input()
    first_result = int(current_match[0])
    second_result = int(current_match[2])
    if first_result > second_result:
        first_team_wins += 1
    elif first_result < second_result:
        first_team_loses += 1
    else:
        first_team_draws += 1

print(f"Team won {first_team_wins} games.")
print(f"Team lost {first_team_loses} games.")
print(f"Drawn games: {first_team_draws}")
