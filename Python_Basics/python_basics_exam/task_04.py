group_one = 0
group_two = 0
group_three = 0

total_food_cost = 0
total_food = 0
food_price = 0.01245

cat_number = int(input())

for cat in range(cat_number):
    cat_consumption = float(input())
    if 100 <= cat_consumption < 200:
        group_one += 1
        total_food += cat_consumption
    elif 200 <= cat_consumption < 300:
        group_two += 1
        total_food += cat_consumption
    elif 300 <= cat_consumption < 400:
        group_three += 1
        total_food += cat_consumption

total_food_cost = food_price * total_food
print(f'Group 1: {group_one} cats.\nGroup 2: {group_two} cats.\nGroup 3: {group_three} cats.\n\
Price for food per day: {total_food_cost:.02f} lv.')
