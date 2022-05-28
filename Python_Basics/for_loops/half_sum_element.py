import sys

n_numbers = int(input())  # the user sets the total number of integers that will be entered
max_num = -sys.maxsize  # stores the biggest number entered
sum_numbers = 0  # sums all entered numbers except the biggest one entered

for i in range(0, n_numbers):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

sum_numbers -= max_num
if max_num == sum_numbers:
    print(f'Yes\nSum = {max_num}')
elif max_num != sum_numbers:
    print(f'No\nDiff = {abs(max_num-sum_numbers)}')





