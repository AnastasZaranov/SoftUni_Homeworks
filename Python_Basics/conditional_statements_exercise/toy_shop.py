puzzle_price, talking_doll_price, teddy_bear_price, minion_price, truck_price = 2.60, 3.00, 4.10, 8.20, 2.00

excursion_cost, puzzle_amount, talking_doll_amount, teddy_bear_amount, minion_amount, truck_amount = float(input()), \
                            int(input()), int(input()), int(input()), int(input()), int(input())

total_article_count = puzzle_amount + talking_doll_amount + teddy_bear_amount + minion_amount + truck_amount
total_article_revenue = puzzle_price * puzzle_amount + talking_doll_price * talking_doll_amount + \
                        teddy_bear_price * teddy_bear_amount + minion_price * minion_amount + truck_price * truck_amount
calc = 0

if total_article_count >= 50:
    total_article_revenue -= total_article_revenue * 0.25
    total_article_revenue -= total_article_revenue * 0.10
else:
    total_article_revenue -= total_article_revenue * 0.10

if total_article_revenue >= excursion_cost:
    calc = total_article_revenue - excursion_cost
    print(f'Yes! {calc:.02f} lv left.')
elif total_article_revenue < excursion_cost:
    calc = excursion_cost - total_article_revenue
    print(f'Not enough money! {calc:.02f} lv needed')
