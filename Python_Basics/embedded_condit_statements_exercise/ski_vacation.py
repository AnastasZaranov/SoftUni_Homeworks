days_stay = int(input())  # 0 to 365
type_of_accommodation = input()   # room for one person, apartment or president apartment
evaluation = input()  # if positive 25%, if negative 10%
total_cost = 0
nights_stay = days_stay - 1

if type_of_accommodation == "room for one person":
    if days_stay < 10:
        total_cost += 18 * nights_stay
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
    if 10 <= days_stay <= 15:
        total_cost += 18 * nights_stay
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
    if days_stay > 15:
        total_cost += 18 * nights_stay
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
elif type_of_accommodation == "president apartment":
    if days_stay < 10:
        total_cost += 35 * nights_stay
        total_cost -= total_cost * 0.10
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
    if 10 <= days_stay <= 15:
        total_cost += 35 * nights_stay
        total_cost -= total_cost * 0.15
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
    if days_stay > 15:
        total_cost += 35 * nights_stay
        total_cost -= total_cost * 0.20
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
elif type_of_accommodation == "apartment":
    if days_stay < 10:
        total_cost += 25 * nights_stay
        total_cost -= total_cost * 0.30
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
    if 10 <= days_stay <= 15:
        total_cost += 25 * nights_stay
        total_cost -= total_cost * 0.35
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
    if days_stay > 15:
        total_cost += 25 * nights_stay
        total_cost -= total_cost * 0.50
        if evaluation == "positive":
            total_cost += total_cost * 0.25
            print(f'{total_cost:.02f}')
        elif evaluation == "negative":
            total_cost -= total_cost * 0.10
            print(f'{total_cost:.02f}')
