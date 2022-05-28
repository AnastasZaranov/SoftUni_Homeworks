# Exercise Nr. 6: Operations between numbers
num_one, num_two = int(input()), int(input())
operators = str(input())
result = 0
# leftover = float(0)

if operators == "+":
    result += num_one + num_two
    if result % 2 == 0:
        print(f'{num_one} {operators} {num_two} = {result} - even')
    else:
        print(f'{num_one} {operators} {num_two} = {result} - odd')
elif operators == "-":
    result += num_one - num_two
    if result % 2 == 0:
        print(f'{num_one} {operators} {num_two} = {result} - even')
    else:
        print(f'{num_one} {operators} {num_two} = {result} - odd')
elif operators == "*":
    result += num_one * num_two
    if result % 2 == 0:
        print(f'{num_one} {operators} {num_two} = {result} - even')
    else:
        print(f'{num_one} {operators} {num_two} = {result} - odd')
elif operators == "/":
    if num_one == 0 or num_two == 0:
        print(f'Cannot divide {num_one} by zero')
    else:
        result += num_one / num_two
        if result % 2 == 0:
            print(f'{num_one} {operators} {num_two} = {result:.2f}')
        else:
            print(f'{num_one} {operators} {num_two} = {result:.2f}')
elif operators == "%":
    if num_one == 0 or num_two == 0:
        print(f'Cannot divide {num_one} by zero')
    else:
        result += num_one % num_two
        print(f'{num_one} {operators} {num_two} = {result}')
