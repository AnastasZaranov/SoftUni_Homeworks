chicken_menu = 10.35
fish_menu = 12.40
veggie_menu = 8.15
delivery = 2.5
dessert = 0.2


chicken_menu_count = int(input())
fish_menu_count = int(input())
veggie_menu_count = int(input())

total = chicken_menu_count * chicken_menu + fish_menu_count * fish_menu + veggie_menu_count * veggie_menu
grand_total = total + total * dessert + delivery
print(round(grand_total, 2))