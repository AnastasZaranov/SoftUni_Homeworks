# Exercise Nr. 5: Journey
budget = float(input())
season = input()
where, destination = "", ""
spend = float(0)

if budget <= 100:
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"

if destination == "Bulgaria":
    if season == "summer":
        where = "Camp"
        spend += budget * 0.30
    elif season == "winter":
        where = "Hotel"
        spend += budget * 0.70
elif destination == "Balkans":
    if season == "summer":
        where = "Camp"
        spend += budget * 0.40
    elif season == "winter":
        where = "Hotel"
        spend += budget * 0.80
else:
    where = "Hotel"
    spend += budget * 0.90

print(f'Somewhere in {destination}\n{where} - {spend:.2f}')