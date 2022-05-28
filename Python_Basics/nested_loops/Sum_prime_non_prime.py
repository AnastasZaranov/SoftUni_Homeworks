flag = False
non_prime = 0
prime = 0

while True:
    entry = input()
    if entry == "stop":
        break

    entry = int(entry)

    if entry < 0:
        print("Number is negative.")

    if entry > 1:
        for i in range(2, entry):
            if entry % i == 0:
                flag = True
                break
        if flag:
            non_prime += entry
            flag = False
        else:
            prime += entry

print(f'Sum of all prime numbers is: {prime}\nSum of all non prime numbers is: {non_prime}')
