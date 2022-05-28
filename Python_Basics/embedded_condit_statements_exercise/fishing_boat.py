# Exercise Nr. 4: fishing boat

budget = int(input())
season = input()
fishermen_count = int(input())
boat_cost = 0

if season == "Spring":
    boat_cost += 3000
if season == "Summer" or season == "Autumn":
    boat_cost += 4200
if season == "Winter":
    boat_cost += 2600

if fishermen_count <= 6:
    boat_cost -= boat_cost * 0.10
elif 7 <= fishermen_count <= 11:
    boat_cost -= boat_cost * 0.15
elif fishermen_count > 11:
    boat_cost -= boat_cost * 0.25

if fishermen_count % 2 == 0 and season != "Autumn":
    boat_cost -= boat_cost * 0.05
    difference = abs(boat_cost - budget)
    if boat_cost > budget:
        print(f'Not enough money! You need {difference:.2f} leva.')
    else:
        print(f'Yes! You have {difference:.2f} leva left.')
else:
    difference = abs(boat_cost - budget)
    if boat_cost > budget:
        print(f'Not enough money! You need {difference:.2f} leva.')
    else:
        print(f'Yes! You have {difference:.2f} leva left.')
