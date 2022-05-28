entry_number = int(input())
flag = False
count_digit = 0

for num in range(1111, 10000):
    count_digit = 0
    flag = False
    number = str(num)
    for digit in range(len(number)):
        divisor = int(number[digit])
        if divisor == 0:
            break
        elif entry_number % divisor != 0:
            flag = True
            break
        else:
            count_digit += 1
            if count_digit == 4:
                print(num, end=" ")
