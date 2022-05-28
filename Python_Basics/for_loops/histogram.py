n_numbers = int(input())
p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for i in range(0, n_numbers):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif num >= 800:
        p5 += 1

print(f'{(p1 / n_numbers) * 100:.02f}%\n{(p2 / n_numbers) * 100:.02f}%\n{(p3 / n_numbers) * 100:.02f}%\n{(p4 / n_numbers) * 100:.02f}%'
      f'\n{(p5 / n_numbers) * 100:.02f}%')