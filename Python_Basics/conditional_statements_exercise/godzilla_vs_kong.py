film_budget, extras_count, costume_cost = float(input()), int(input()), float(input())
film_decor = film_budget * 0.10
total_film_cost = 0


if extras_count > 150:
    costume_cost -= costume_cost * 0.10
    total_film_cost = film_decor + costume_cost * extras_count
else:
    total_film_cost = film_decor + costume_cost * extras_count

if total_film_cost > film_budget:
    print(f'Not enough money! \nWingard needs {total_film_cost - film_budget:.02f} leva more')
elif total_film_cost < film_budget:
    print(f'Action! \nWingard starts filming with {film_budget - total_film_cost:.02f} leva left')

