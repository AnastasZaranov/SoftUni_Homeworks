pen_package = 5.8
marker_package = 7.2
cleaning_solution = 1.2

pen_count = int(input())
marker_count = int(input())
solution_litres = int(input())
percentage_discount = int(input())/100

total = pen_count * pen_package + marker_count * marker_package + cleaning_solution * solution_litres
grand_total = total - total * percentage_discount
print(grand_total)