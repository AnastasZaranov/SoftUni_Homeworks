climber_groups = int(input())

g1, g2, g3, g4, g5 = 0, 0, 0, 0, 0
total_climbers = 0
for climber in range(0, climber_groups):
    climber_count = int(input())
    if climber_count <= 5:
        g1 += climber_count
        total_climbers += climber_count
    elif 5 < climber_count <= 12:
        g2 += climber_count
        total_climbers += climber_count
    elif 12 < climber_count <= 25:
        g3 += climber_count
        total_climbers += climber_count
    elif 25 < climber_count <= 40:
        g4 += climber_count
        total_climbers += climber_count
    elif climber_count > 40:
        g5 += climber_count
        total_climbers += climber_count
p1, p2, p3, p4, p5 = g1/total_climbers, g2/total_climbers, g3/total_climbers, g4/total_climbers, g5/total_climbers
print(f'{p1 * 100:.02f}%\n{p2 * 100:.02f}%\n{p3 * 100:.02f}%\n{p4 * 100:.02f}%\n{p5 * 100:.02f}%')

