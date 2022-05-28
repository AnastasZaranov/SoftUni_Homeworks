#  03. Computer Room
#  Write a program which calculates the price per person per hour  and the total sum spent on the room

month = input()  # Enter march, april, may, june, july, august
hours_spent = int(input())  # total hours spent in the room
group_count = int(input())  # total number of people present
time_of_day = input()  # Either day or night

price_per_person = 0
total_cost = 0

month_a = "march, april, may"
month_b = "june, july, august"

#  For a group_count >= 4 people, the price per person decreases with 10%
#  For hours_spent >= 5 hours, the price per person decreases with 50%

group_discount = 1 # 1.00 means no discount
hours_discount = 1 # 1.00 means no discount
#  From March to May the cost of the room per person is 10.50 BGN (if day) or 8.40 BGN (if night)
#  From June to August the cost of the room per person is 12.60 BGN (if day) or 10.20 BGN (if night)

if group_count >= 4:
    group_discount = 0.10
else:
    group_discount = 1.00

if hours_spent >= 5:
    hours_discount = 0.50
else:
    hours_discount = 1.00


if month in month_a:
    pass
    if time_of_day == "day":
        #  price per person 10.50 BGN w/o discounts
        price_per_person = 10.50 * group_discount
        price_per_person = price_per_person * hours_discount
        total_cost = price_per_person * group_count * hours_spent
        print(f'Price per person for one hour: {price_per_person:.02f}')
        print(f'Total cost of the visit: {total_cost:.02f}')

    elif time_of_day == "night":
        #  price per person 8.40 BGN w/o discounts
        price_per_person = 8.40 - 8.40 * group_discount
        price_per_person = price_per_person - price_per_person * hours_discount
        total_cost = price_per_person * group_count * hours_spent
        print(f'Price per person for one hour: {price_per_person:.02f}')
        print(f'Total cost of the visit: {total_cost:.02f}')
elif month in month_b:
    pass
    if time_of_day == "day":
        #  price per person 12.60 BGN w/o discounts
        price_per_person = 12.60 - 12.60 * group_discount
        price_per_person = price_per_person - price_per_person * hours_discount
        total_cost = price_per_person * group_count * hours_spent
        print(f'Price per person for one hour: {price_per_person:.02f}')
        print(f'Total cost of the visit: {total_cost:.02f}')
    elif time_of_day == "night":
        #  price per person 10.20 BGN w/o discounts
        price_per_person = 10.20 - 10.20 * group_discount
        price_per_person = price_per_person - price_per_person * hours_discount
        total_cost = price_per_person * group_count * hours_spent
        print(f'Price per person for one hour: {price_per_person:.02f}')
        print(f'Total cost of the visit: {total_cost:.02f}')

