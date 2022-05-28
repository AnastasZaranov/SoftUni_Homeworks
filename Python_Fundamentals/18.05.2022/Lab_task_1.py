num = float(input())

if num == 0:
    print("zero")
elif num > 0:
    if 1 > abs(num) > 0:
        print("small positive")
    elif abs(num) > 1000000:
        print("large positive")
    else:
        print("positive")
elif num < 0:
    if 1 > abs(num) > 0:
        print("small negative")
    elif abs(num) > 1000000:
        print("large negative")
    else:
        print("negative")
