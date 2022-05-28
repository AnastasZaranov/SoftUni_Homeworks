number_one = int(input())
number_two = int(input())
odd_sum = 0
even_sum = 0

for num in range(number_one, number_two + 1):
    odd_sum = 0
    even_sum = 0
    for x in range(len(str(num))):
        if x % 2 == 0:
            even_sum += int(str(num)[x])
        else:
            odd_sum += int(str(num)[x])

    if odd_sum == even_sum:
        print(str(num), end=" ")
    else:
        pass
