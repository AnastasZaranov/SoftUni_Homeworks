flower_type = input()  # Enter Roses, Dahlias, Tulips, Narcissus or Gladiolus
flower_count = int(input())
budget = int(input())
cost = 0

if flower_type == "Roses":
    cost += 5 * flower_count
    if flower_count > 80:
        cost -= cost * 0.10
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")
    else:
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")

if flower_type == "Dahlias":
    cost += 3.80 * flower_count
    if flower_count > 90:
        cost -= cost * 0.15
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")
    else:
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")

if flower_type == "Tulips":
    cost += 2.80 * flower_count
    if flower_count > 80:
        cost -= cost * 0.15
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")
    else:
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")

if flower_type == "Narcissus":
    cost += 3 * flower_count
    if flower_count < 120:
        cost += cost * 0.15
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")
    else:
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")

if flower_type == "Gladiolus":
    cost += 2.50 * flower_count
    if flower_count >= 80:
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")
    else:
        cost += cost * 0.20
        if cost > budget:
            print(f"Not enough money, you need {cost - budget:.2f} leva more.")
        else:
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} "
                  f"leva left.")
