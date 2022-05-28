protective_nylon_sqm_price = 1.50
paint_price_per_litre = 14.5
paint_thinner_per_litre = 5.00

nylon_addon_sqm = 2
paint_addon_litre_percentage = 0.1
bag_price = 0.4
handwork_cost_factor = 0.3

sqm_nylon = int(input())
litre_paint = int(input())
litre_thinner = int(input())
total_work_hours = int(input())

total_nylon = (sqm_nylon + nylon_addon_sqm) * protective_nylon_sqm_price
total_paint = (litre_paint + (litre_paint * paint_addon_litre_percentage)) * paint_price_per_litre
total_thinner = litre_thinner * paint_thinner_per_litre

material_total = total_nylon + total_paint + total_thinner + bag_price
grand_total = material_total + (material_total * handwork_cost_factor) * total_work_hours

print(grand_total)


