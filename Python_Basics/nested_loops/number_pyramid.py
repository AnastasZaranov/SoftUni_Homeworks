num = int(input())
is_number_bigger_than_num = False
number = 1

for row in range(1, num + 1):
    if number > num:
        is_number_bigger_than_num = True
        break

    for col in range(1, row + 1):
        print(str(number), end=" ")
        number += 1
        if number > num:
            is_number_bigger_than_num = True
            break
    print()