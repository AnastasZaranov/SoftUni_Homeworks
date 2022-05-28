enter_number = int(input())
bonus = 0

if enter_number <= 100:
    bonus += 5
elif 100 < enter_number <= 1000:
    bonus += 0.2 * enter_number
elif enter_number > 1000:
    bonus = 0.1 * enter_number + bonus

if enter_number % 2 == 0:
    bonus += 1
elif enter_number % 10 == 5 or enter_number == 5:
    bonus += 2

total = enter_number + bonus
print(bonus)
print(total)