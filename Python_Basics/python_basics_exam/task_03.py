
month = input()
hours = int(input())
group = int(input())
day_time = input()

group_discount: float = 1.00
hours_discount: float = 1.00

price_per_person_per_hour = 0
total_price = 0

if group >= 4:
    group_discount = 0.9
else:
    group_discount = 1

if hours >= 5:
    hours_discount = 0.5
else:
    hours_discount = 1


if month == "march":
    day_hour = 10.50
    night_hour = 8.40
    if day_time == "day":
        price_per_person_per_hour = day_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')
    elif day_time == "night":
        price_per_person_per_hour = night_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')


elif month == "april":
    day_hour = 10.50
    night_hour = 8.40
    if day_time == "day":
        price_per_person_per_hour = day_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')
    elif day_time == "night":
        price_per_person_per_hour = night_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')


elif month == "may":
    day_hour = 10.50
    night_hour = 8.40
    if day_time == "day":
        price_per_person_per_hour = day_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')
    elif day_time == "night":
        price_per_person_per_hour = night_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')


elif month == "june":
    day_hour = 12.60
    night_hour = 10.20
    if day_time == "day":
        price_per_person_per_hour = day_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')
    elif day_time == "night":
        price_per_person_per_hour = night_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')


elif month == "july":
    day_hour = 12.60
    night_hour = 10.20
    if day_time == "day":
        price_per_person_per_hour = day_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')
    elif day_time == "night":
        price_per_person_per_hour = night_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')


elif month == "august":
    day_hour = 12.60
    night_hour = 10.20
    if day_time == "day":
        price_per_person_per_hour = day_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')
    elif day_time == "night":
        price_per_person_per_hour = night_hour * group_discount
        price_per_person_per_hour = price_per_person_per_hour * hours_discount

        total_price = price_per_person_per_hour * group * hours
        print(f'Price per person for one hour: {price_per_person_per_hour:.02f}')
        print(f'Total cost of the visit: {total_price:.02f}')
