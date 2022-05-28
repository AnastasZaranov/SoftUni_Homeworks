price_per_sqm = 7.61
discount_percentage = 0.18
sqm_for_greenery = int(input())
gross_cost = price_per_sqm * sqm_for_greenery
net_discount = gross_cost * discount_percentage
net_cost = gross_cost - net_discount


print(f'The final price is: {net_cost} lv.'
    f'The discount is: {net_discount} lv.')