food_bought = int(input())
food_bought = food_bought * 1000
food_consumed = 0

is_not_adopted = True

while is_not_adopted:
    daily_food_consumption = input()
    if daily_food_consumption == "Adopted":
        is_not_adopted = False
    else:
        daily_food_consumption = int(daily_food_consumption)
        food_consumed += daily_food_consumption

diff = abs(food_consumed - food_bought)

if food_consumed > food_bought:
    print(f'Food is not enough. You need {diff} grams more.')
else:
    print(f'Food is enough! Leftovers: {diff} grams.')


