tournament_participation_number = int(input())
tournament_points_base = int(input())
tournament_points = 0
tournament_count = 0
win_count = 0

for tournament in range(0, tournament_participation_number):
    achievement = input()
    tournament_count += 1
    if achievement == "W":
        tournament_points += 2000
        win_count += 1
    elif achievement == "F":
        tournament_points += 1200
    elif achievement == "SF":
        tournament_points += 720

print(f'Final points: {tournament_points + tournament_points_base}\nAverage points: {tournament_points//tournament_count}'
      f'\n{(win_count/tournament_count) * 100:.02f}%')

