actors_name = input()
academy_points = float(input())
academy_voters = int(input())
threshold = 1250.50

for voter in range(0, academy_voters):
    voter_name = input()
    multiplier = len(voter_name)
    voter_points = ((float(input()) * multiplier)/2)
    academy_points += voter_points
    if academy_points > threshold:
        print(f'Congratulations, {actors_name} got a nominee for leading role with {academy_points:.01f}!')
        break

if academy_points < threshold:
    print(f'Sorry, {actors_name} you need {threshold - academy_points:.01f} more!')
