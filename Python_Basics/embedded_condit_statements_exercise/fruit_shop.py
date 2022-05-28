day_of_week = str(input("Please enter day of week: "))
fruit = str(input("Please enter fruit: "))
quantity = float(input("Please enter desired quantity: "))

if day_of_week in "Monday, Tuesday, Wednesday, Thursday, Friday":
    if fruit == "banana":
        cost = 2.50
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "apple":
        cost = 1.20
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "orange":
        cost = 0.85
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "grapefruit":
        cost = 1.45
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "kiwi":
        cost = 2.70
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "pineapple":
        cost = 5.50
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "grapes":
        cost = 3.85
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    else:
        print("error")
elif day_of_week in "Saturday, Sunday":
    if fruit == "banana":
        cost = 2.70
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "apple":
        cost = 1.25
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "orange":
        cost = 0.90
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "grapefruit":
        cost = 1.60
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "kiwi":
        cost = 3.00
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "pineapple":
        cost = 5.60
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    elif fruit == "grapes":
        cost = 4.20
        total_cost = cost * quantity
        print(f'{total_cost:.02f}')
    else:
        print("error")
