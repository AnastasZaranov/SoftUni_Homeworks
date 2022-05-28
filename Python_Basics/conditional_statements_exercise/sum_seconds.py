first, second, third = int(input()), int(input()), int(input())
sum_seconds = first + second + third
minutes = sum_seconds // 60
seconds = sum_seconds % 60

print(f'{minutes}:{seconds:02d}')
