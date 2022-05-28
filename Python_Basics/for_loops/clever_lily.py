lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

even_b_day_count = 1
toy_count = 0
b_day_cash = 0
brother_cash = 0
total_cash = 0


for year in range(1, lily_age + 1):
    if year % 2 == 0:
        b_day_cash += 10 * even_b_day_count
        brother_cash += 1
        even_b_day_count += 1
    elif year % 2 != 0:
        toy_count += 1

total_cash += b_day_cash - brother_cash + toy_count * toy_price
if total_cash >= washing_machine_price:
    print(f'Yes! {total_cash - washing_machine_price:.02f}')
elif total_cash < washing_machine_price:
    print(f'No! {washing_machine_price - total_cash:.02f}')


