hour, minutes = int(input()), int(input())
time = hour * 60 + minutes + 15
hour_time = time // 60
minutes_time = time % 60

if hour_time == 24:
    hour_time = 0
elif hour_time > 24:
    hour_time %= 24

print(f'{hour_time}:{minutes_time:02d}')