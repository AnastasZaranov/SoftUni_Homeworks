locations = int(input())
mined = 0
running_average = 0

for location in range(locations):
    planned_average = float(input())
    mining_days = int(input())
    mined = 0
    running_average = 0
    for day in range(mining_days):
        mined_per_day = float(input())
        mined += mined_per_day
        running_average = mined / mining_days
        if day + 1 == mining_days:
            diff = abs(planned_average - running_average)
            if planned_average <= running_average:
                print(f'Good job! Average gold per day: {running_average:.02f}.')
            else:
                print(f'You need {diff:.02f} gold.')
        else:
            continue
