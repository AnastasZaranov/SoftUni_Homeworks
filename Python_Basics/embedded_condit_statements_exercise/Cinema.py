premiere_price = 12.00
normal_price = 7.50
discount_price = 5.00

film_type, row_count, column_count = str(input("Please enter the type of movie being projected: ")), \
                                     int(input("Please enter number of rows: ")), \
                                     int(input("Please enter number of columns: "))

revenue = 0
attendance = 0

if film_type == "Premiere":
    attendance = row_count * column_count
    revenue += attendance * premiere_price
    print(f'{revenue:.2f} leva')
elif film_type == "Normal":
    attendance = row_count * column_count
    revenue += attendance * normal_price
    print(f'{revenue:.2f} leva')
elif film_type == "Discount":
    attendance = row_count * column_count
    revenue += attendance * discount_price
    print(f'{revenue:.2f} leva')
else:
    print("Something went wrong!")
